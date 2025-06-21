
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
        msg.innerText = mensajes[index].mensaje;
        document.getElementById('chatContainer').appendChild(msg);

        setTimeout(() => { msg.classList.add('visible'); }, 50);

        setTimeout(() => {
            index++;
            iniciarChat();
        }, mensajes[index].tiempo);
    }
}

async function startRecording() {
    let stream = await navigator.mediaDevices.getDisplayMedia({ video: { frameRate: 30 } });
    let recorder = new MediaRecorder(stream);
    let chunks = [];

    recorder.ondataavailable = e => chunks.push(e.data);
    recorder.onstop = () => {
        let blob = new Blob(chunks, { type: 'video/webm' });
        let url = URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'video_chatgpt.webm';
        a.click();
    };

    recorder.start();

    let duracionTotal = mensajes.reduce((acc, cur) => acc + cur.tiempo, 0) + 2000;
    setTimeout(() => {
        recorder.stop();
        stream.getTracks().forEach(track => track.stop());
    }, duracionTotal);
}

window.onload = cargarConversacion;
