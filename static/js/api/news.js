//construir a lista de recursos
function buildNewsList(link) {

    let news = document.getElementById('noticias')
    let info = document.getElementById('informacoes')

    let url = 'https://nlei.up.railway.app/api/news-list/'
    //console.log('last: ', "http://127.0.0.1:8000/api/news-list/?p=last")

    if (typeof (link) != "undefined") {
        url = link
    }
    //console.log('link: ', link)

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            //console.log('Data:', data)

            let list = data.results

            //pode-se usar data["results"] ou data.results

            //list corresponde á lista de recursos


            listarNews(list)

            function listarNews(listaDeNews) {

                for (const i in listaDeNews) {
                    let item

                    let data_noticia = new Date(listaDeNews[i].data) 

                    //ver se os artigos têm imagem
                    if ((listaDeNews[i].imagelink == "") && (listaDeNews[i].imagem == null)) {
                        item = `
                        <article class="noticia">
                            <h2>${listaDeNews[i].cabecalho}</h2>
                            <div>
                                <p> ${listaDeNews[i].corpo}</p>
                            </div>
                            <span class="data">Data: ${data_noticia.toUTCString()}</span>
        
                        </article>`
                    } else {
                        let link

                        if (listaDeNews[i].imagelink != "") {
                            link = listaDeNews[i].imagelink
                        } else {
                            link = 'https://nlei.up.railway.app/static' + listaDeNews[i].imagem
                        }

                        item = `            
                        <article class="noticia">
                            <h2>${listaDeNews[i].cabecalho}</h2>
                            <div>
                                <img src=${link} alt="${listaDeNews[i].cabecalho}">
                                <p>${listaDeNews[i].corpo}</p>
                            </div>
                            <span class="data">Data: ${data_noticia.toUTCString()}</span>
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

            //paginação
            let paginacao_div = document.getElementById("pagination")
            let last_page = Math.ceil(data.count / (data.results).length)

            function paginacao() {

                let link_paginas = ''

                for (let p = 1; p < last_page + 1; p++) {
                    //console.log('pagina=', p)

                    const pagina = `
                        <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/news-list/?p=${p}')">${p}</a>
                    `
                    link_paginas += pagina


                }

                function pegarNumeroDePagina(url_desejado) {
                    //console.log('novo url: ', url_desejado)

                    const searchParams = new URLSearchParams(url_desejado.search);

                    return searchParams.get('p')
                }
                const next_link = data.next
                const prev_link = data.previous
                //console.log(next_link)
                const newurl = new URL(next_link)

                const pagAtual = parseInt(pegarNumeroDePagina(newurl)) - 1
                const pagAnterior = pagAtual - 1
                const pagSeguinte = parseInt(pegarNumeroDePagina(newurl))


                printLink = (p) => {
                    return `
                        <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/news-list/?p=${p}')">${p}</a>
                        
                        `;
                }
                //se tiver mais do que 5 paginas a serem paginadas
                if (last_page > 5) {
                    //se tem pagina seguinte e anterior
                    if ((data.next != null) && (data.previous != null)) {

                        imprimirLinks(printLink(pagAnterior), printLink(pagAtual), printLink(pagSeguinte))

                    }
                    // se tem pagina seguinte mas não tem anterior
                    else if ((data.next != null) && (data.previous == null)) {


                        imprimirLinks(pag_atual = printLink(pagAtual), pag_seguinte = printLink(pagSeguinte))

                    }
                    // se tem pagina anterior mas não tem pagina seguinte 
                    else if ((data.next == null) && (data.previous != null)) {


                        imprimirLinks(pag_atual = printLink(pagAnterior + 1), pag_anterior = printLink(pagAnterior))

                    } else {
                        //deixar a div de paginas vazia
                        paginacao_div.innerHTML = ''
                    }
                    //console.log('mais de 5 paginas')
                    function imprimirLinks(
                        pag_anterior = '',
                        pag_atual = '',
                        pag_seguinte = '') {

                        paginacao_div.innerHTML = `
                    <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/news-list/?p=1')">&laquo;</a>
                    ${pag_anterior}
                    ${pag_atual}
                    ${pag_seguinte}                    
                    <a href="" onclick="mudarLink('https://nlei.up.railway.app/api/news-list/?p=last')">&raquo;</a>
    
                    `
                    }

                } else {
                    //console.log('menos de 5 paginas')
                    paginacao_div.innerHTML = ''
                    paginacao_div.innerHTML = `
                    <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/news-list/?p=1')">&laquo;</a>
                    ${link_paginas}
                    <a href="" onclick="mudarLink('https://nlei.up.railway.app/api/news-list/?p=last')">&raquo;</a>
    
                    `
                }
                addactiveclass(pagAtual)
            }
            paginacao()


        })
}

buildNewsList()

function mudarLink(link) {
    document.getElementById('noticias').innerHTML = ''
    document.getElementById('informacoes').innerHTML = ''
    buildNewsList(link)
}

//adicionar classe active na paginação
function addactiveclass(pag_atual) {
    let lista_de_links = document.querySelectorAll('#pagination a')

    for (const pag of lista_de_links) {
        if (parseInt(pag.innerHTML) == pag_atual) {
            pag.classList += 'active'
        }
    }
}
