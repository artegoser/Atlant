const Downloader = require("../js/downloader");
let downloader = new Downloader();
const fs = require("fs");

window.addEventListener("load",async ()=>{
    function updateinf(perc, proc){
        document.getElementById("progress").style.width = perc+"%"
        document.getElementById("procname").innerHTML = proc;
    }
    async function downloadmodel(){
        if(require("../../td-2.0.json").usermodified===true){
            updateinf(100, "Skipping download a lang model because it modified...");
            return
        }

        let procname = "Download lang model"
        let percentupdate = setInterval(()=>{
            updateinf(downloader.percent, procname);
        }, 0);
        await downloader.downloadHttp("https://raw.githubusercontent.com/artegoser/tardis-v3/master/td-2.0.json", "./td-2.0.json");
        updateinf(100, procname);
        clearInterval(percentupdate);
    }
    function compilemodel(){
        let procname = "Compiling lang model"
        const { NlpManager } = require('node-nlp');
        const manager = new NlpManager({ languages: ['ru', 'en']});
        let compiler = require("../js/nlp-compiler");
        let dataset = JSON.parse(fs.readFileSync("./td-2.0.json", "utf-8"));
        updateinf(0, procname);
        compiler(manager, dataset);
        updateinf(100, procname);
    }

    await downloadmodel();
    compilemodel();
    updateinf(100, "Done...")
    window.location.replace("./index.html");
});