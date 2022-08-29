
function buildRecursoList() {
    let files = document.getElementById('files')

    let url = 'http://127.0.0.1:8000/api/recursos-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            console.log('Data:', data)

            let list = data


            for (const i in list) {
                console.log(list[i])

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


            }
        })
}

buildRecursoList()