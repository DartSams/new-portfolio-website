function setActive (id) {
    console.log(id)
    var navBar = document.getElementById("nav-bar").childNodes;
    var i;
    for (i = 0; i < navBar.length; i++) {
        navBar[i+=1].style.backgroundColor = "";
        let activeButton;
        activeButton = document.getElementById(id);
        activeButton.style.backgroundColor="rgb(121,  97, 248)"

    }        
}

function expand (id) {
    let el = document.getElementById(id);
    el.style.height = "300px";
    el.style.width = "1000px";
    el.setAttribute('onclick','contract(id)')
}

function contract(id) {
    let el = document.getElementById(id);
    el.style.height = "40px";
    el.style.width = "120px";
    el.setAttribute('onclick','expand(id)')
}