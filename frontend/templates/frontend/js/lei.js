


    //selecionar um ano especifico 

    var opcao = document.getElementById("select")

    opcao.addEventListener('change', mudarAno)

    function mudarAno() {
        switch (opcao.value) {
            case "ano0":
                document.getElementById("div2").style.display="none"
                document.getElementById("div1").style.display="block"
                break;
            case "ano1":
                document.getElementById("div1").style.display="none"
                document.getElementById("div2").style.display="block"
                break
            default:

                document.getElementById("div1").style.display="block"
                document.getElementById("div2").style.display="block"

                break;
        }
    }
