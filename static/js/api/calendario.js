
//const CLIENT_ID = '712098284825-rraotf8tm94trhoatkn0nipvhkg5v0d2.apps.googleusercontent.com';
//const API_KEY = 'AIzaSyD1N8VmWiA0UDlsNvX7JK-Wx9dleDbSVOg';


function buildCalendarioList() {
    let events = document.getElementById('eventos')

    let url = 'http://127.0.0.1:8000/api/calendario-list/'

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            console.log('Data:', data)



            let eventos = data


            const weekday = ["Domingo","Segunda-feira","Terça-Feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado"];



            //iterar nos grupos de turma
            for (const evento of eventos) {

                let fullDate = evento.dataInicio
                console.log(fullDate)
                
                const dia = new Date(fullDate).getDate()
                //let diaString = (new Date(fullDate).toUTCString().split(',')[0])
                let mes = (new Date(fullDate).toDateString().split(' ')[1].toUpperCase())
                let horainicio = (new Date(fullDate).toLocaleTimeString())
                let horafim = (new Date(evento.dataFim).toLocaleTimeString())
      
                console.log('mes: ', mes)

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
                            <p>${evento.detallhe}
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


