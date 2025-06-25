import tkinter as tk
from tkinter import scrolledtext

# Definir la plantilla HTML en una variable
plantilla = """<div class="actividad" id="actividad#actividad">
    <h2>Actividad #actividad:</h2>

    <h3>📝 Enunciado</h3>
    <p>#enunciado</p>

    <h3>✅ Resultado</h3>
    <div class="resultado">
      #html
    </div>

    <h3>💻 Código</h3>
    <pre><code class="language-html">
      #codigo
    </code></pre>
    </div>"""

def procesar_texto():
    texto_integrar = texto_text.get("1.0", tk.END).strip()
    enunciado = enunciado_text.get().strip()
    actividad_num = actividad_entry.get().strip()
    
    # Reemplazar #html en la plantilla con el texto a integrar
    resultado_html = plantilla.replace("#html", texto_integrar)
    
    # Reemplazar #enunciado en la plantilla con el enunciado
    resultado_html = resultado_html.replace("#enunciado", enunciado)
    
    # Reemplazar #actividad en la plantilla con el número de actividad
    resultado_html = resultado_html.replace("#actividad", actividad_num)
    
    # Escapar etiquetas < y >
    texto_escapado = texto_integrar.replace("<", "&lt;").replace(">", "&gt;")
    
    # Reemplazar #codigo en la plantilla con el texto escapado
    resultado_html = resultado_html.replace("#codigo", texto_escapado)
    
    # Mostrar el resultado en el área de texto de salida
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, resultado_html)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Herramienta HTML")

# Crear widgets
tk.Label(ventana, text="Número de Actividad:").pack(fill=tk.X)
actividad_entry = tk.Entry(ventana)
actividad_entry.pack(fill=tk.X)

tk.Label(ventana, text="Enunciado:").pack(fill=tk.X)
enunciado_text = tk.Entry(ventana)
enunciado_text.pack(fill=tk.X)

tk.Label(ventana, text="Texto a integrar:").pack(fill=tk.X)
texto_text = scrolledtext.ScrolledText(ventana, width=50, height=10)
texto_text.pack(fill=tk.BOTH, expand=True)

tk.Button(ventana, text="Ejecutar", command=procesar_texto).pack(fill=tk.X)

tk.Label(ventana, text="Resultado:").pack(fill=tk.X)
resultado_text = scrolledtext.ScrolledText(ventana, width=50, height=10)
resultado_text.pack(fill=tk.BOTH, expand=True)

# Iniciar el bucle principal
ventana.mainloop()
