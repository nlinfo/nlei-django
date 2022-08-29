
function buildNotaList() {
    let notas = document.getElementById('notas')

    let url = 'http://127.0.0.1:8000/api/notas-list/'

    fetch(url)
    .then((response) => response.json())
    .then(function(data) {
        console.log('Data:', data)

        let list = data


        for (const i in list) {
            console.log(list[i].turma.turma)


        }
    })
}

buildNotaList()