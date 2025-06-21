
let index = 0;
let mensajes = [];

async function cargarConversacion() {
    let response = await fetch('conversacion.json');
    let data = await response.json();
    mensajes = data.conversacion;
    iniciarChat();
}

function iniciarChat() {
    if (index < mensajes.length) {
        let msg = document.createElement('div');
        msg.classList.add('mensaje');
        msg.classList.add(mensajes[index].autor);

        if (mensajes[index].autor === 'chatgpt') {
            msg.innerHTML = 'ChatGPT is typing<span class="cursor"></span>';
            document.getElementById('chatContainer').appendChild(msg);
            scrollToBottom();
            setTimeout(() => {
                mostrarTextoLetraPorLetra(msg, mensajes[index].mensaje, () => {
                    msg.classList.add('visible');
                    index++;
                    setTimeout(iniciarChat, 1000);
                });
            }, 1000);
        } else {
            msg.innerText = mensajes[index].mensaje;
            document.getElementById('chatContainer').appendChild(msg);
            setTimeout(() => { msg.classList.add('visible'); scrollToBottom(); }, 50);
            setTimeout(() => {
                index++;
                iniciarChat();
            }, mensajes[index].tiempo);
        }
    }
}

function mostrarTextoLetraPorLetra(elemento, texto, callback) {
    let i = 0;
    elemento.innerHTML = '';

    let cursor = document.createElement('span');
    cursor.classList.add('cursor');
    elemento.appendChild(cursor);

    let interval = setInterval(() => {
        cursor.before(texto.charAt(i));
        i++;
        scrollToBottom();
        if (i >= texto.length) {
            clearInterval(interval);
            cursor.remove();
            if (callback) callback();
        }
    }, 30);
}

function scrollToBottom() {
    let chatContainer = document.getElementById('chatContainer');
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

window.onload = cargarConversacion;
