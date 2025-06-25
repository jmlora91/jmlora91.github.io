const teclas = document.querySelectorAll(".tecla");
const sonido = document.getElementById("tecla-sound");

// Reproduce el sonido y añade la clase 'pulsada' a la tecla
function pulsar(teclaEl) {
  sonido.currentTime = 0;
  sonido.play();
  teclaEl.classList.add("pulsada");
  setTimeout(() => teclaEl.classList.remove("pulsada"), 100);
}

teclas.forEach((tecla) => {
  tecla.addEventListener("mousedown", () => pulsar(tecla));
});

document.addEventListener("keydown", (e) => {
  let key = e.key === " " ? " " : e.key;
  key = key.length === 1 ? key.toUpperCase() : key;
  /**
   * Finds the corresponding key element from the teclas array based on the provided key event.
   * The search is performed by matching the text content of the element, 
   * checking for the space key, or matching the data-key attribute.
   *
   * @type {HTMLElement | undefined} 
   * @param {KeyboardEvent} e - The keyboard event containing the key information.
   * @param {Array<HTMLElement>} teclas - An array of key elements to search through.
   * @returns {HTMLElement | undefined} The found key element or undefined if not found.
   */
  const teclaEl = [...teclas].find(
    (el) =>
      el.textContent.trim().toUpperCase() === key.toUpperCase() ||
      (e.key === " " && el.textContent.trim() === "Espacio") ||
      el.dataset.key === e.key
  );
  if (teclaEl) pulsar(teclaEl);
});

// Cambia entre modo oscuro y claro
/**
 * Toggles between dark and light mode for the webpage.
 * Updates the text of the mode switch and synchronizes the checkbox state.
 *
 * @function toggleModo
 * @returns {void}
 */
function toggleModo() {
  document.body.classList.toggle("dark");
  const switchTexto = document.getElementById("modoTexto");
  const modoActivo = document.body.classList.contains("dark");

  // Actualiza el texto para mostrar el modo al que se va a cambiar
  switchTexto.textContent = modoActivo ? "Modo claro" : "Modo oscuro";

  // Sincroniza el checkbox si se cambia por código
  document.getElementById("modoSwitch").checked = modoActivo;
}

// Filtra las actividades y enlaces del menú según el texto ingresado
/**
 * Filtra los enlaces del menú y las actividades en el contenido
 * según el texto ingresado en el campo de filtro.
 * 
 * Esta función obtiene el valor del campo de entrada, lo convierte
 * a minúsculas y oculta o muestra los elementos de acuerdo a si
 * su texto incluye el filtro.
 * 
 * @function
 * @returns {void}
 */
function filtrarTodo() {
  const input = document.getElementById("filtro-menu");
  const filtro = input.value.toLowerCase();

  // Filtrar enlaces del menú
  const enlaces = document.querySelectorAll("#lista-actividades a");
  enlaces.forEach((enlace) => {
    const texto = enlace.textContent.toLowerCase();
    enlace.style.display = texto.includes(filtro) ? "block" : "none";
  });

  // Filtrar actividades en el contenido
  const actividades = document.querySelectorAll(".actividad");
  actividades.forEach((actividad) => {
    const textoActividad = actividad.innerText.toLowerCase();
    actividad.style.display = textoActividad.includes(filtro)
      ? "block"
      : "none";
  });
}

// Configura el texto del switch al cargar
window.addEventListener("DOMContentLoaded", () => {
  const modoActivo = document.body.classList.contains("dark");
  document.getElementById("modoTexto").textContent = modoActivo
    ? "Modo claro"
    : "Modo oscuro";
  document.getElementById("modoSwitch").checked = modoActivo;
});
