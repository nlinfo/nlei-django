//construir a lista de recursos
function buildNewsList() {

    let news = document.getElementById('noticias')
    let info = document.getElementById('informacoes')

    let url = 'http://127.0.0.1:8000/api/news-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            console.log('Data:', data)

            let list = data

            //list corresponde á lista de recursos

            listarNews(list)

            function listarNews(listaDeNews) {

                for (const i in listaDeNews) {
                    let item

                    //ver se os artigos têm imagem
                    if ((listaDeNews[i].imagelink == "") && (listaDeNews[i].imagem == null)) {
                        item = `
                        <article class="noticia">
                            <h2>${listaDeNews[i].cabecalho}</h2>
                            <div>
                                <p> ${listaDeNews[i].corpo}</p>
                            </div>
                            <span class="data">Data: ${listaDeNews[i].data}</span>
        
                        </article>`
                    } else {
                        let link

                        if (listaDeNews[i].imagelink != "") {
                            link = listaDeNews[i].imagelink
                        } else {
                            link = 'http://127.0.0.1:8000/static' + listaDeNews[i].imagem
                        }

                        item = `            
                        <article class="noticia">
                            <h2>${listaDeNews[i].cabecalho}</h2>
                            <div>
                                <img src=${link} alt="${listaDeNews[i].cabecalho}">
                                <p>${listaDeNews[i].corpo}</p>
                            </div>
                            <span class="data">Data: ${listaDeNews[i].data}</span>
                        </article>`
                    }

                    //verificar se é informação
                    if (listaDeNews[i].informacao == false) {
                        news.innerHTML += item
                    } else {
                        info.innerHTML += item
                    }

                }
            }


        })
}

buildNewsList()