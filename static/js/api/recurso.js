
//construir a lista de recursos
function buildRecursoList(link) {
    let files = document.getElementById('files')

    let url = 'https://nlei.up.railway.app/api/recursos-list/'

    if (typeof (link) != "undefined") {
        url = link
    }
    //console.log('link: ', link)

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            //console.log('Data:', data)

            let list = data.results
            //console.log(list)

            //list corresponde á lista de recursos

            listarRecursos(list)

            function listarRecursos(listaDeDados) {

                for (const i in listaDeDados) {
                    //console.log(listaDeDados[i].id)

                    let item = `
                        <a class="recurso" onclick="abrirDownload(); downloadFile(${listaDeDados[i].id})" >
                            <i class="fa-solid fa-folder-open"></i>
                            <div>
                                <p>${listaDeDados[i].nome}</p>
                                <span>${listaDeDados[i].cadeira.nome}</span>
                                <span>${listaDeDados[i].anoletivo.data}</span>
                            </div>
                        </a>`

                    files.innerHTML += item

                }
            }

            fetch('https://nlei.up.railway.app/api/allrecursos-list/')
                .then((response) => response.json())
                .then(function (lista_completa_de_recursos) {
                    //console.log(lista_completa_de_recursos)


                    // search bar

                    let searchbar = document.querySelector('#bara_de_pesquisa')

                    searchbar.addEventListener('keyup', function () {
                        const value = this.value
                        const filteredData = searchTable(value, lista_completa_de_recursos)

                        //console.log('Value:', value)
                        //console.log(filteredData)
                        files.innerHTML = ''
                        //console.log('filtered:', filteredData)
                        if (filteredData.length == 0) {
                            files.innerHTML += `<p>Nenhum arquivo encontrado</p>`
                        }
                        listarRecursos(filteredData)
                    })


                    function searchTable(value, data) {
                        let filteredData = []

                        for (const recurso of data) {
                            value = value.toLowerCase()
                            let name = recurso.nome.toLowerCase()

                            if (name.includes(value)) {
                                filteredData.push(recurso)
                            }
                        }

                        return filteredData
                    }

                    //filter section

                    let FiltrarButton = document.getElementById("filtrarRecurso")
                    let pesquisar = document.getElementById("pesquisar")
                    pesquisar.addEventListener('click', (event) => {
                        event.preventDefault()
                    })

                    FiltrarButton.addEventListener('click', () => {

                        let anoLectivo = document.getElementById("ano_lectivo").value
                        let cadeira = document.getElementById("selectCadeira").value.toLowerCase()

                        //console.log(anoLectivo, cadeira)
                        files.innerHTML = ''
                        listarRecursos(filterSession(cadeira, anoLectivo, lista_completa_de_recursos))

                        //fechar a session depois de filtrar
                        FiltrarButton.addEventListener("click", () => {
                            filtroSection.style.visibility = "hidden";
                        })
                    })

                    function filterSession(cadeira, anoLectivo, data) {
                        let filteredData = []

                        for (const recurso of data) {
                            let recursoCadeira = recurso.cadeira.nome.toLowerCase()
                            let recursoAno = recurso.anoletivo.data
                            //console.log(recursoCadeira, recursoAno)

                            if (recursoCadeira.includes(cadeira) && recursoAno.includes(anoLectivo)) {
                                filteredData.push(recurso)
                            }
                        }

                        return filteredData
                    }


                    /*preencher os selects de ano e cadeira*/
                    function preencherSelects(lista_completa_de_recursos) {

                        let anoLectivo = document.getElementById("ano_lectivo")
                        let cadeiraSelect = document.getElementById("selectCadeira")

                        let ano = new Set(), cadeira = new Set()

                        for (const recurso of lista_completa_de_recursos) {
                            let recursoCadeira = recurso.cadeira.nome
                            let recursoSilga = recurso.cadeira.sigla
                            let recursoAno = recurso.anoletivo.data
                            //console.log(recursoCadeira, recursoAno, 'preencher')

                            let _ano = '' , _cadeira = ''
                            if (!(ano.has(recursoAno))) {
                                _ano = `<option value="${recursoAno}">${recursoAno}</option>`
                            }

                            if (!(cadeira.has(recursoSilga))) {
                                _cadeira = `<option value="${recursoSilga}">${recursoCadeira}</option>`
                            }

                            ano.add(recursoAno)
                            cadeira.add(recursoSilga)

                            anoLectivo.innerHTML += _ano
                            cadeiraSelect.innerHTML += _cadeira

                        }

                    }
                    preencherSelects(list)
                })




            /*paginação*/

            let paginacao_div = document.getElementById("pagination")
            let last_page = Math.ceil(data.count / (data.results).length)

            function paginacao() {

                let link_paginas = ''

                for (let p = 1; p < last_page + 1; p++) {
                    //console.log('pagina=', p)

                    const pagina = `
                        <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/recursos-list/?p=${p}')">${p}</a>
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
                        <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/recursos-list/?p=${p}')">${p}</a>
                        
                        `;
                }
                console.log(last_page)
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
                    <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/recursos-list/?p=1')">&laquo;</a>
                    ${pag_anterior}
                    ${pag_atual}
                    ${pag_seguinte}                    
                    <a href="" onclick="mudarLink('https://nlei.up.railway.app/api/recursos-list/?p=last')">&raquo;</a>
    
                    `
                    }

                } else {
                    //console.log('menos de 5 paginas')
                    paginacao_div.innerHTML = ''
                    paginacao_div.innerHTML = `
                    <a href="#" onclick="mudarLink('https://nlei.up.railway.app/api/recursos-list/?p=1')">&laquo;</a>
                    ${link_paginas}
                    <a href="" onclick="mudarLink('https://nlei.up.railway.app/api/recursos-list/?p=last')">&raquo;</a>
    
                    `
                }
                addactiveclass(pagAtual)
            }

            paginacao()






        })
}

function mudarLink(link) {
    document.getElementById('files').innerHTML = ''
    buildRecursoList(link)
}

buildRecursoList()

//adicionar classe active na paginação
function addactiveclass(pag_atual) {
    let lista_de_links = document.querySelectorAll('#pagination a')
    //console.log(lista_de_links)
    //console.log((parseInt(lista_de_links[1].innerHTML)))

    for (const pag of lista_de_links) {
        //console.log('1-log',pag.innerHTML, 'tipo:',typeof(parseInt(pag.innerHTML)));
        //console.log('2-log',parseInt(pag.innerHTML))

        if (parseInt(pag.innerHTML) == pag_atual) {
            //console.log(parseInt(pag.innerHTML),' é atual')
            pag.classList += 'active'
            //console.log(pag.classList)
        }
    }
}
//addactiveclass()




//pegar um recurso especifico
function downloadFile(ID) {
    let baixarFicheiro = document.getElementById('baixar_ficheiro')

    //const params = new URLSearchParams(window.location.search);
    //const recursoID = params.get("fileId");
    //console.log('url:', recursoID)
    //console.log(ID)

    let url = `https://nlei.up.railway.app/api/recursos-detail/${ID}/`

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            //console.log('Recurso:', data)

            let recurso = data

            let nomeDoficheiro = document.getElementById("nomeDoFicheiro")
            let nomeDacadeira = document.getElementById("nomeDaCadeira")
            let nomeDodocente = document.getElementById("nomeDoDocente")
            let anolectivo = document.getElementById("Ano_Letivo")

            nomeDoficheiro.innerHTML = recurso.nome;
            nomeDacadeira.innerHTML = recurso.cadeira.nome;
            const docente = recurso.docente
            if (docente != null) {
                nomeDodocente.innerHTML = recurso.docente.nome
            } else {
                nomeDodocente.innerHTML = 'recurso sem docente'
            }

            anolectivo.innerHTML = recurso.anoletivo.data

            const link = 'https://nlei.up.railway.app/static' + recurso.ficheiro;
            let buttonLink = document.getElementById("baixar_ficheiro")
            buttonLink.innerHTML = `<a href=${link} download>Download</a>`

        })
}
//downloadFile()