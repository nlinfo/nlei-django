
function buildNotaList() {
    let notas = document.getElementById('notas')

    let url = 'https://nlei.up.railway.app/api/notas-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            //console.log('Data:', data)

            let NotaTurma = data
            //NotaTurma : notas agrupadas por turma

            let chavesturma = Object.keys(NotaTurma)
            //console.log('chaves: ', chavesturma)

            //iterar nos grupos de turma
            for (const chave in chavesturma) {

                let todasasnotas = '', turma
                //iterar em cada turma dentro do grupo
                for (const turma of NotaTurma[chavesturma[chave]]) {

                    const link = 'https://nlei.up.railway.app/static' + turma.ficheiro

                    let nota = `
                    <a href=${link}><i class="fa-solid fa-file"></i>${turma.titulo}</a>
                    `
                    todasasnotas += nota
                    //console.log(turma.titulo)
                    
                }

                turma = `
                <div class="turma"id="turma${chave}">
                    <h3>Turma ${chavesturma[chave]}</h3>
                    ${todasasnotas}
                </div>
                `
                //console.log(chavesturma[chave])

                notas.innerHTML += turma
            }
            //console.log(NotaTurma['A'])
        })
}

buildNotaList()