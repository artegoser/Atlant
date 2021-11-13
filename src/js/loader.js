const Downloader = require("../js/downloader");
let downloader = new Downloader();

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

    await downloadmodel();
    // updateinf(100, "Done...")
    setInterval(()=>window.location.replace("./index.html"), 2000);
});