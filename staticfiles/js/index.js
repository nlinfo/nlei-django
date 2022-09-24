


//links
const abrir_fecharLinksRapidos = document.getElementById("ellips_xmark")

abrir_fecharLinksRapidos.addEventListener("click", abrir_fecharLinks);


//função para abrir e fechar a div dos links
function abrir_fecharLinks() {

    let icone_id = document.querySelector('#abrir_fecharLinks')
    let divComLinks = document.querySelector("#divComLinks")

    icone_id.style.background = "#3B3B3B";
    icone_id.classList.toggle("fa-xmark");

    if (divComLinks.style.display == "none") {

        divComLinks.style.display = "flex"
        icone_id.style.background = "#de5151";
    } else {
        divComLinks.style.display = "none"
    }

}


