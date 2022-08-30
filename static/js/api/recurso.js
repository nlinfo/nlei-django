
function buildRecursoList() {
    let files = document.getElementById('files')

    let url = 'http://127.0.0.1:8000/api/recursos-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            console.log('Data:', data)

            let list = data
            //list corresponde á lista de recursos


            for (const i in list) {
                //console.log(list[i])

                let item = `
                    <a class="recurso" href="#download?fileId=1">
                        <i class="fa-solid fa-folder-open"></i>
                        <span>
                            <p>${list[i].nome}</p>
                            <span>${list[i].cadeira.nome}</span>
                            <span>${list[i].anoletivo.data}</span>
                        </span>
                    </a>`

                files.innerHTML += item

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
                    buildRecursoList(filteredData)
                })


                function searchTable(value, data) {
                    var filteredData = []

                    for (let i = 0; i < data.length; i++) {
                        value = value.toLowerCase()
                        let name = data[i].nome.toLowerCase()

                        if (name.includes(value)) {
                            filteredData.push(data[i])
                        }
                    }

                    return filteredData
                }


            }
        })
}

buildRecursoList()