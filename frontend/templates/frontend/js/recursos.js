

//filter section
const abrir_filtro = document.querySelector("#abrir_filtro")

const fechar_filtro = document.querySelector("#fechar_filtro")
const filtroSection = document.querySelector("#filtro")

abrir_filtro.addEventListener("click", function abrir_f() {
    filtroSection.style.visibility="visible" ;
})
fechar_filtro.addEventListener("click", () => {
    filtroSection.style.visibility="hidden" ;
})


//download file section

const abrir_download = document.querySelector(".recurso")
const fechar_download = document.querySelector("#fechar_download")
const downloadSection = document.querySelector("#download") 

var allResourceButtons = document.querySelectorAll('a[class^=recurso]');

/*pegar todos os links de recurso*/
for (var i = 0; i < allResourceButtons.length; i++) {
    allResourceButtons[i].addEventListener('click', function() {
      console.clear();
      console.log("You clicked:", this.innerHTML);

      /*abrir a sessão de download*/
      downloadSection.style.visibility="visible" ;
  
    });
  }


  fechar_download.addEventListener("click", () => {
    downloadSection.style.visibility="hidden" ;
})
