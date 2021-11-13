const fs = require("fs");

window.addEventListener("load", ()=>{
    let switcher = document.getElementById("theme-switcher");
    let theme = document.getElementById("theme");
    if(localStorage.getItem("theme") === "light") {
        switcher.checked = true;
        theme.href = "../css/light.css";
    } else if(localStorage.getItem("theme") === "black"){
        switcher.checked = false;
        theme.href = "../css/black.css";
    }
    switcher.onchange = ()=>{
        localStorage.setItem("theme", switcher.checked === true ? "light" : "black");
        if(switcher.checked === true){
            fs.writeFileSync("./src/css/theme.css", `@import "./light.css"`);
        } else{
            fs.writeFileSync("./src/css/theme.css", `@import "./black.css"`);
        }
        theme.href = switcher.checked === true ? "../css/light.css" : "../css/black.css";
    }
});