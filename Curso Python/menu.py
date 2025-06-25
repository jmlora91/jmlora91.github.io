import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time

class MacButton(tk.Canvas):
    """Clase que representa un botón personalizado con esquinas redondeadas."""
    
    def __init__(self, master, text, command=None, width=140, height=100, icon=None, tooltip=None):
        """Inicializa el botón con texto, comando, tamaño, icono y tooltip."""
        super().__init__(master, width=width, height=height, highlightthickness=0, bg=master["bg"])
        self.command = command
        self.text = text
        self.icon = icon
        self.tooltip = tooltip
        self.configure(cursor="hand2")
        self.radius = 15  # Radio para las esquinas redondeadas
        self.padding = 10
        self.bind("<Button-1>", self.on_click)  # Evento de clic
        self.bind("<Enter>", self.on_enter)      # Evento al entrar
        self.bind("<Leave>", self.on_leave)      # Evento al salir
        self.draw_button(normal=True)            # Dibuja el botón en estado normal

        if tooltip:
            self.tip = ToolTip(self, tooltip)    # Tooltip si se proporciona
        else:
            self.tip = None

    def draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        """Dibuja un rectángulo con esquinas redondeadas."""
        points = [
            x1+r, y1,
            x1+r, y1,
            x2-r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y1+r,
            x2, y2-r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x2-r, y2,
            x1+r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y2-r,
            x1, y1+r,
            x1, y1+r,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def draw_button(self, normal=True):
        """Dibuja el botón en su estado normal o presionado."""
        self.delete("all")
        if normal:
            self.draw_rounded_rect(5, 5, 135, 95, self.radius, fill="#e0e0e5", outline="#bfbfc2")
            self.draw_rounded_rect(0, 0, 130, 90, self.radius, fill="#f5f5f7", outline="#d0d0d5")
        else:
            self.draw_rounded_rect(5, 5, 135, 95, self.radius, fill="#c7c7cc", outline="#9e9ea3")
            self.draw_rounded_rect(0, 0, 130, 90, self.radius, fill="#e6e6e8", outline="#b0b0b3")

        if self.icon:
            self.create_image(65, 30, image=self.icon)  # Dibuja el icono

        self.create_text(65, 75, text=self.text, font=("San Francisco", 12, "normal"), fill="#1d1d1f")

    def on_click(self, event):
        """Maneja el evento de clic en el botón."""
        if self.command:
            self.command()

    def on_enter(self, event):
        """Maneja el evento de entrada del mouse sobre el botón."""
        self.draw_button(normal=False)

    def on_leave(self, event):
        """Maneja el evento de salida del mouse del botón."""
        self.draw_button(normal=True)


class ToolTip:
    """Clase para mostrar un tooltip (mensaje emergente) para un widget."""
    
    def __init__(self, widget, text):
        """Inicializa el tooltip con el widget asociado y el texto."""
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.widget.bind("<Enter>", self.show_tip)  # Evento para mostrar el tooltip
        self.widget.bind("<Leave>", self.hide_tip)  # Evento para ocultar el tooltip

    def show_tip(self, event=None):
        """Muestra el tooltip en la posición del mouse."""
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 10
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#f5f5f7", relief=tk.SOLID, borderwidth=1,
                         font=("San Francisco", 10), fg="#3c3c43")
        label.pack(ipadx=5, ipady=3)

    def hide_tip(self, event=None):
        """Oculta el tooltip."""
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class App(tk.Tk):
    """Clase principal de la aplicación que hereda de Tkinter."""
    
    def __init__(self):
        """Inicializa la aplicación y configura la ventana principal."""
        super().__init__()
        self.title("Ejecutor de Scripts Python")
        self.geometry("700x500")
        self.minsize(500, 400)

        # Cambiado para evitar error de fuente:
        # Si no tienes San Francisco, usa Helvetica
        try:
            self.option_add("*Font", ("San Francisco", 13))
        except tk.TclError:
            self.option_add("*Font", ("Helvetica", 13))

        self.configure(bg="#f0f0f5")

        self.ruta_base = ""

        self.crear_menu()  # Crea el menú de la aplicación

        self.frame_scripts = tk.Frame(self, bg="#f0f0f5")
        self.frame_scripts.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame_scripts, bg="#f0f0f5", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.frame_scripts, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f5")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w",
                                   background="#e1e1e6", fg="#3c3c43", font=("Helvetica", 11))
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        # Icono python (base64 embebido)
        self.icono_py = tk.PhotoImage(data="""
            R0lGODlhEAAQAMQfAFVVVfDw8MDAwJ+fn7e3t8LCwsbGxuHh4S4uLoqKioiIiLe3t6Ghoa+vr4aGhqWlpWJi
            YhQUFPX19S8vL4uLio6Ojt7e3rS0tLq6usLCwqOjo1NTU2BgYF1dXXFxcX9/f////wAAAAAAAAAAAAAAAAAA
            AAAAAAAAACH5BAEAAB8ALAAAAAAQABAAAAVf4CeOZGmeaKqubOu+cCzPdBFCpD7nHxiEEAz5Hg4PBQgOEwMZ
            QHq4DwLhkAJsDMjzOA4IQAyhK4gEQAADs=
        """)

        self.botones_scripts = []

        self.seleccionar_carpeta()  # Selecciona la carpeta al iniciar

    def crear_menu(self):
        """Crea el menú de la aplicación."""
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Seleccionar carpeta", command=self.seleccionar_carpeta)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

    def seleccionar_carpeta(self):
        """Permite al usuario seleccionar una carpeta que contenga scripts Python."""
        ruta = tk.filedialog.askdirectory(title="Selecciona la carpeta con scripts Python")
        if ruta:
            self.ruta_base = ruta
            self.status_var.set(f"Carpeta seleccionada: {ruta}")
            self.cargar_scripts()  # Carga los scripts de la carpeta seleccionada
        else:
            self.status_var.set("No se seleccionó ninguna carpeta")

    def cargar_scripts(self):
        """Carga los scripts Python de la carpeta seleccionada y crea botones para ejecutarlos."""
        for btn in self.botones_scripts:
            btn.destroy()  # Destruye botones existentes
        self.botones_scripts.clear()

        if not self.ruta_base:
            return

        archivos = [f for f in os.listdir(self.ruta_base) if f.endswith(".py") and os.path.isfile(os.path.join(self.ruta_base, f))]
        if not archivos:
            self.status_var.set("No se encontraron archivos .py en la carpeta seleccionada")
            return

        self.status_var.set(f"{len(archivos)} archivos encontrados")

        columnas = 4  # Número de columnas para los botones
        for idx, archivo in enumerate(archivos):
            fila = idx // columnas
            columna = idx % columnas
            ruta_archivo = os.path.join(self.ruta_base, archivo)
            modificado = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(ruta_archivo)))
            tooltip_text = f"{ruta_archivo}\nModificado: {modificado}"

            btn = MacButton(self.scrollable_frame, text=archivo, icon=self.icono_py,
                            command=lambda a=archivo: self.ejecutar_archivo(a),
                            tooltip=tooltip_text)
            btn.grid(row=fila, column=columna, padx=15, pady=15, sticky="nsew")
            self.botones_scripts.append(btn)

        for col in range(columnas):
            self.scrollable_frame.grid_columnconfigure(col, weight=1)

    def ejecutar_archivo(self, archivo):
        """Ejecuta el archivo Python seleccionado en una terminal."""
        ruta = os.path.join(self.ruta_base, archivo)
        self.status_var.set(f"Ejecutando {archivo}...")

        try:
            if sys.platform.startswith("darwin"):  # macOS
                comando = f'osascript -e \'tell app "Terminal" to do script "python3 \\"{ruta}\\""\'' 
                subprocess.Popen(comando, shell=True)

            elif os.name == "nt":  # Windows
                subprocess.Popen(f'start cmd /k python "{ruta}"', shell=True)

            elif os.name == "posix":  # Linux
                try:
                    subprocess.Popen(['gnome-terminal', '--', 'python3', ruta])
                except FileNotFoundError:
                    subprocess.Popen(['x-terminal-emulator', '-e', f'python3 "{ruta}"'])
            self.status_var.set(f"Ejecutado {archivo}")
        except Exception as e:
            self.status_var.set(f"Error ejecutando {archivo}: {e}")
            messagebox.showerror("Error", f"No se pudo ejecutar {archivo}:\n{e}")

if __name__ == "__main__":
    app = App()  # Crea y ejecuta la aplicación
    app.mainloop()
