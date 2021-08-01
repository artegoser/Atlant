const { NlpManager } = require('node-nlp');
const manager = new NlpManager({ languages: ['ru', 'en']});
manager.load("./tardis.nlp");

window.addEventListener("load", ()=>{

    document.getElementById("send").onclick = getresp

    document.getElementById("message").onkeydown = (e)=>{
        if(e.key === "Enter") getresp()
    }

    function addin(text){
        let div = document.createElement('div');
        div.className = "row chat-text in-chat";
        div.innerHTML = `<div class="col"><div class="row">TARDIS</div><div class="row">${text}</div></div>`;
        document.getElementById("chat-body").append(div);
    }
    function addout(text){
        let div = document.createElement('div');
        div.className = "row chat-text out-chat";
        div.innerHTML = `<div class="col">${text}</div>`;
        document.getElementById("chat-body").append(div);
    }
    async function getresp(){
        let message = document.getElementById("message");
        addout(message.value);
        const response = await manager.process(message.value);
        if(response.intent==="help.version") response.answer += "TARDIS 3.0.0-alpha";
        addin(response.answer||"Извините я не понял");
        message.value = "";
    }
});