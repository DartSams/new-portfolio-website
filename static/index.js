function setActive (id) {
    showMobileNav()
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
    el.innerHTML = "";
    createCurrentProject(id)
}

function contract(id) {
    let el = document.getElementById(id);
    el.style.cssText = `
        height:60px;
        width:150px;
    `
    el.setAttribute('onclick','expand(id)')
    el.innerHTML = "";

    let title = document.createElement("div");
    title.style.cssText =  `
        display:flex;
        justify-content:space-around;
        align-items:baseline;
    `

    let img1 = document.createElement("img");
    img1.src = "static/images/down.png";
    img1.style.width = "10px"
    img1.style.height = "15px"

    let p = document.createElement("p");
    p.innerHTML = "Current Project"

    let img2 = document.createElement("img")
    img2.src = "static/images/down.png";
    img2.style.width = "10px"
    img2.style.height = "15px"

    title.appendChild(p)
    p.before(img1)
    title.appendChild(img2)

    el.style.background = ""

    setTimeout(function(){
        el.appendChild(title);
    },2000)
}

function createCurrentProject (id) {
    let element = document.getElementById(id);
    element.style.background = "rgb(121,  97, 248)";

    let header = document.createElement("h2");
    header.innerHTML = "Current Project"

    let currentProjectDiv = document.createElement("div");
    currentProjectDiv.style.cssText = `
        display:flex;
        justify-content:space-around;
        align-content:center;
    `;
    
    let img = document.createElement("img");
    img.src = "static/images/project_preview/portfolio website preview.png"
    img.style.width = "300px"

    let description = document.createElement("div");
    description.setAttribute("class","currentProjectDescription")
    description.style.cssText = `
        display:flex;
        flex-direction:column;
    `;

    let descriptionHeader = document.createElement("h4");
    descriptionHeader.innerHTML = "Portfolio website"
    descriptionHeader.style.cssText = `
        font-size:20px;
        border-bottom:2px solid white
    `

    let descriptionText = document.createElement("p");
    descriptionText.innerHTML = "This website."


    setTimeout(function(){
        element.appendChild(header);
        element.appendChild(currentProjectDiv)
        currentProjectDiv.appendChild(img)
        currentProjectDiv.appendChild(description)
        description.appendChild(descriptionHeader)
        description.appendChild(descriptionText)
    },2000)
}

function openPopup () {
    let popupContainer = document.getElementById("popup-container")
    popupContainer.style.display = "flex"
}

function closePopup () {
    let popupContainer = document.getElementById("popup-container")
    popupContainer.style.display = "none"
}

function showMobileNav() {
    let openSideBar=document.getElementById("sidebar");
    if (openSideBar.style.left < "0px") {
        openSideBar.style.left = "0px"
    } else {
        openSideBar.style.cssText ="left:-310px"
    }
}