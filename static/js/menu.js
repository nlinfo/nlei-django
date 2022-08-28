
var botaoMenu = document.querySelector("#botao_menu")
var menuMobile = document.querySelector('#menu_mobile')

botaoMenu.addEventListener("click", abrir_fecharMenu);

function abrir_fecharMenu() {
    menuMobile.classList.toggle("menu_mobile");
}