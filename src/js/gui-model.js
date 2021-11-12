const { NlpManager } = require('node-nlp');
const manager = new NlpManager({ languages: ['ru', 'en']});
let compiler = require("../js/nlp-compiler");
let dataset = JSON.parse(fs.readFileSync("./td-2.0.json", "utf-8"));
compiler(manager, dataset);

window.addEventListener("load", ()=>{
    document.getElementById("send").onclick = () => {
        dataset[document.getElementById()]
    }
});
