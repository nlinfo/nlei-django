


//selecionar um ano especifico 

const opcao = document.getElementById("select")

opcao.addEventListener('change', mudarAno)

function mudarAno() {
    switch (opcao.value) {
        case "ano0":
            document.getElementById("div1").style.display = "block"
            document.getElementById("div2").style.display = "none"
            document.getElementById("div3").style.display = "none"
            document.getElementById("div4").style.display = "none"
            document.getElementById("div5").style.display = "none"

            break;
        case "ano1":
            
            document.getElementById("div1").style.display = "none"
            document.getElementById("div2").style.display = "block"
            document.getElementById("div3").style.display = "none"
            document.getElementById("div4").style.display = "none"
            document.getElementById("div5").style.display = "none"

            break
        case "ano2":
            document.getElementById("div1").style.display = "none"
            document.getElementById("div2").style.display = "none"
            document.getElementById("div3").style.display = "block"
            document.getElementById("div4").style.display = "none"
            document.getElementById("div5").style.display = "none"
            break
        case "ano3":
            document.getElementById("div1").style.display = "none"
            document.getElementById("div2").style.display = "none"
            document.getElementById("div3").style.display = "none"
            document.getElementById("div4").style.display = "block"
            document.getElementById("div5").style.display = "none"
            break
        case "ano4":
            document.getElementById("div1").style.display = "none"
            document.getElementById("div2").style.display = "none"
            document.getElementById("div3").style.display = "none"
            document.getElementById("div4").style.display = "none"
            document.getElementById("div5").style.display = "block"
            break
        default:

            document.getElementById("div1").style.display = "block"
            document.getElementById("div2").style.display = "block"
            document.getElementById("div3").style.display = "block"
            document.getElementById("div4").style.display = "block"
            document.getElementById("div5").style.display = "block"

            break;
    }
}
