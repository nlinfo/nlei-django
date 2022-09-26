
function buildCalendarioList() {
    let events = document.getElementById('eventos')

    let url = 'https://nlei.up.railway.app/api/calendario-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            //console.log('Data:', data)



            let eventos = data


            const weekday = ["Domingo","Segunda-feira","Terça-Feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado"];



            //iterar nos grupos de turma
            for (const evento of eventos) {

                let fullDate = evento.dataInicio
                //console.log(fullDate)
                
                const dia = new Date(fullDate).getDate()
                //let diaString = (new Date(fullDate).toUTCString().split(',')[0])
                let mes = (new Date(fullDate).toDateString().split(' ')[1].toUpperCase())
                let horainicio = (new Date(fullDate).toLocaleTimeString())
                let horafim = (new Date(evento.dataFim).toLocaleTimeString())
      
                //console.log('mes: ', mes)

                //console.log(dataAMD)

                let event = `
                <div class="evento">
                    <div>
                        <span>${mes}</span>
                        <span>${dia}</span>
                    </div>
                    <div>
                        <span>${weekday[new Date(fullDate).getUTCDay()]}, ${horainicio}-${horafim}</span>
                        <span>${evento.titulo}</span>
                        <details>
                            <summary>Detalhes:</summary>
                            <p>${evento.detalhe}
                            </p>
                        </details>
                        <a href="#">Ver evento</a>
                    </div>
                </div>
                `
                events.innerHTML += event




            }
        })
}

buildCalendarioList()


