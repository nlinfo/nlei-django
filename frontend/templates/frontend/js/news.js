
var input = document.querySelector("#informacao")

var informacao = document.querySelector("#info_button")
var news = document.querySelector("#news_button")

var infoSection = document.querySelector("#informacoes")
var newsSection = document.querySelector("#noticias")



informacao.addEventListener('click', ()=>{
    input.checked = true
    informacaoToggle()
    //console.log(input.checked )
})

news.addEventListener('click', ()=>{
    input.checked = false
    informacaoToggle()
    //console.log(input.checked )
})



//mostrar as sessoes de info ou news

function informacaoToggle() {

    if (input.checked) {
        infoSection.style.display = "block"
        newsSection.style.display = "none"
    } else {
        infoSection.style.display = "none"
        newsSection.style.display = "block" 
    }
}
informacaoToggle()

