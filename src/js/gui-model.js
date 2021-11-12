const { NlpManager } = require('node-nlp');
const manager = new NlpManager({ languages: ['ru', 'en']});
let compiler = require("../js/nlp-compiler");
let dataset = JSON.parse(fs.readFileSync("./td-2.0.json", "utf-8"));
compiler(manager, dataset);

window.addEventListener("load", ()=>{
    document.getElementById("send").onclick = () => {
        dataset[document.getElementById("typeofm").value][document.getElementById("lang").value][document.getElementById("type").value].push(document.getElementById("item").value)
        fs.writeFileSync("./td-2.0.json", JSON.stringify(dataset, null, "  "));
        compiler(manager, dataset);
    }
});