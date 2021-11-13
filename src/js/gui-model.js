const { NlpManager } = require('node-nlp');
const manager = new NlpManager({ languages: ['ru', 'en']});
let compiler = require("../js/nlp-compiler");
let dataset = JSON.parse(fs.readFileSync("./td-2.0.json", "utf-8"));
compiler(manager, dataset);

window.addEventListener("load", ()=>{
    function updatetypes(){
        let types = new Set(Object.keys(dataset.questions.ru).concat(Object.keys(dataset.questions.en)).concat(Object.keys(dataset.answers.en)).concat(Object.keys(dataset.answers.ru)));
        document.getElementById("types").value = Array.from(types).join("\n");
    }
    updatetypes();
    document.getElementById("send").onclick = () => {
        dataset.usermodufied = true;
        dataset[document.getElementById("typeofm").value][document.getElementById("lang").value][document.getElementById("type").value] = dataset[document.getElementById("typeofm").value][document.getElementById("lang").value][document.getElementById("type").value] || [];
        dataset[document.getElementById("typeofm").value][document.getElementById("lang").value][document.getElementById("type").value].push(document.getElementById("item").value)
        fs.writeFileSync("./td-2.0.json", JSON.stringify(dataset, null, "  "));
        compiler(manager, dataset);
        updatetypes();
    }
});