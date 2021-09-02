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
        div.className = "row chat-text in-chat animate__fadeInLeft";
        div.id = "toanim";
        div.innerHTML = `<div class="col"><div class="row">TARDIS</div><div class="row">${text}</div></div>`;
        document.getElementById("chat-body").append(div);
        document.getElementById("toanim").classList.add('animate__animated');
        document.getElementById("toanim").id = "anim";
        window.scrollTo(0, document.body.scrollHeight)
    }
    function addout(text){
        let div = document.createElement('div');
        div.className = "row chat-text out-chat animate__fadeInLeft";
        div.id = "toanim";
        div.innerHTML = `<div class="col">${text}</div>`;
        document.getElementById("chat-body").append(div);
        document.getElementById("toanim").classList.add('animate__animated');
        document.getElementById("toanim").id = "anim";
        window.scrollTo(0, document.body.scrollHeight)
    }
    async function getresp(){
        let message = document.getElementById("message");
        addout(message.value);
        const response = await manager.process(message.value);
        message.value = "";
        setTimeout(()=>{
            if(response.intent==="help.version") response.answer += "TARDIS 3.0.0-alpha";
            addin(response.answer||"Извините я не понял");
        }, 500);
    }
});