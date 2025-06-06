    // Función para abrir el modal y mostrar la imagen ampliada
    function openModal(img) {
      const modal = document.getElementById("modal");
      const modalImg = document.getElementById("modalImage");

      modal.style.display = "flex"; // Muestra el modal
      modalImg.src = img.src; // Pone la imagen ampliada en el modal
    }

    // Función para cerrar el modal
    function closeModal() {
      const modal = document.getElementById("modal");
      modal.style.display = "none"; // Oculta el modal
    }