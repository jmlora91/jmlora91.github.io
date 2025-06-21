
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
            msg.innerText = 'ChatGPT is typing...';
            document.getElementById('chatContainer').appendChild(msg);
            setTimeout(() => {
                msg.innerText = mensajes[index].mensaje;
                msg.classList.add('visible');
                index++;
                setTimeout(iniciarChat, mensajes[index - 1].tiempo);
            }, 1000);
        } else {
            msg.innerText = mensajes[index].mensaje;
            document.getElementById('chatContainer').appendChild(msg);
            setTimeout(() => { msg.classList.add('visible'); }, 50);
            setTimeout(() => {
                index++;
                iniciarChat();
            }, mensajes[index].tiempo);
        }
    }
}

window.onload = cargarConversacion;
