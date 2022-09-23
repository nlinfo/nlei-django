//important for service worker

// Registering Service Worker
window.addEventListener('load', () =>{
    registerSW()
})

async function registerSW(){
    if('serviceWorker' in navigator){
        try{
            await navigator.serviceWorker.register('../../static/js/sw.js')
            console.log('SW registred!')
        } catch(e){
            console.log('SW registration failed!');
        }
    }
}