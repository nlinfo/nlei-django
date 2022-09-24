

//filter section
const abrir_filtro = document.querySelector("#abrir_filtro")

const fechar_filtro = document.querySelector("#fechar_filtro")
const filtroSection = document.querySelector("#filtro")

abrir_filtro.addEventListener("click", function abrir_f() {
  filtroSection.style.visibility = "visible";
})
fechar_filtro.addEventListener("click", () => {
  filtroSection.style.visibility = "hidden";
})


//download file section

const abrir_download = document.querySelector(".recurso")
const fechar_download = document.querySelector("#fechar_download")
const downloadSection = document.querySelector("#download")


fechar_download.addEventListener("click", () => {
  downloadSection.style.visibility = "hidden";
})


function abrirDownload() {
  //abrir a sessão de download
  downloadSection.style.visibility = "visible";
}

//let allResourceButtons = document.querySelectorAll('a[class^=recurso]');




