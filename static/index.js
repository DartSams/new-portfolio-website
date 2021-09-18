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