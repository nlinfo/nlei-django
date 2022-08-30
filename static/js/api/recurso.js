

//construir a lista de recursos
function buildRecursoList() {
    let files = document.getElementById('files')

    let url = 'http://127.0.0.1:8000/api/recursos-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            console.log('Data:', data)

            let list = data

            //list corresponde á lista de recursos

            listarRecursos(list)

            function listarRecursos(listaDeDados) {

                for (const i in listaDeDados) {
                    //console.log(list[i])

                    let item = `
                        <a class="recurso" href="#download?fileId=1">
                            <i class="fa-solid fa-folder-open"></i>
                            <span>
                                <p>${listaDeDados[i].nome}</p>
                                <span>${listaDeDados[i].cadeira.nome}</span>
                                <span>${listaDeDados[i].anoletivo.data}</span>
                            </span>
                        </a>`

                    files.innerHTML += item

                }
            }


            // search bar

            let searchbar = document.querySelector('#bara_de_pesquisa')

            searchbar.addEventListener('keyup', function () {
                const value = this.value
                const filteredData = searchTable(value, list)

                console.log('Value:', value)
                console.log(filteredData)
                files.innerHTML = ''
                console.log('filtered:', filteredData)
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
                event.preventDefault()})

            FiltrarButton.addEventListener('click', () => {

                let anoLectivo = document.getElementById("ano_lectivo").value
                let cadeira = document.getElementById("selectCadeira").value.toLowerCase()

                console.log(anoLectivo, cadeira)
                files.innerHTML = ''
                listarRecursos(filterSession(cadeira, anoLectivo, list))

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
                    console.log(recursoCadeira, recursoAno)

                    if (recursoCadeira.includes(cadeira) && recursoAno.includes(anoLectivo)) {
                        filteredData.push(recurso)
                    }
                }

                return filteredData
            }






            /*preencher os selects de ano e cadeira*/
            function preencherSelects(lista) {

                let anoLectivo = document.getElementById("ano_lectivo")
                let cadeiraSelect = document.getElementById("selectCadeira")

                for (const recurso of lista) {
                    let recursoCadeira = recurso.cadeira.nome
                    let recursoSilga = recurso.cadeira.sigla
                    let recursoAno = recurso.anoletivo.data
                    console.log(recursoCadeira, recursoAno, 'preencher')

                    let ano = `<option value="${recursoAno}">${recursoAno}</option>`
                    console.log('ano feito')

                    let cadeira = `<option value="${recursoSilga}">${recursoCadeira}</option>`

                    anoLectivo.innerHTML += ano
                    cadeiraSelect.innerHTML += cadeira 
                    
                }

            }
            preencherSelects(list)

        })
}

buildRecursoList()