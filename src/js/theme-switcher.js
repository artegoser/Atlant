window.addEventListener("load", ()=>{
    let switcher = document.getElementById("theme-switcher");
    let theme = document.getElementById("theme");
    if(localStorage.getItem("theme") === "light"){
        theme.href = "../css/light.css";
        switcher.checked = true;
    } else{
        theme.href = "../css/black.css";
    }
    switcher.onchange = ()=>{
        localStorage.setItem("theme", switcher.checked === true ? "light" : "black");
        theme.href = switcher.checked === true ? "../css/light.css" : "../css/black.css";
    }
});