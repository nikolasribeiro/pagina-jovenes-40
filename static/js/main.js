window.addEventListener('load', main);

function main(){

    /* MenuBar */
    const nav = document.querySelector('.nav');
    const toggleCollapse = document.querySelector('.toggle-collapse');
    
    // Llamamos a la funcion de callback cuando el usuario hace click en el burger
    toggleCollapse.addEventListener('click', ()=>{
        nav.classList.toggle('collapse');
    });

    /* Script que muestra la fecha importante del dia de hoy */
    let today = new Date();
    let day = String(today.getDate()).padStart(2, '0');
    //console.log(day);
    const importantDates = document.querySelectorAll('.lista-items');
    
    importantDates.forEach(element => {
        if(element.innerHTML.includes(day)){
            //console.log(element.className);
            element.className += " hoy";
        }
    });

    /* funcionalidad para ir al contenido de la web */
    const btn_explorar = document.querySelector('#explorar');
    btn_explorar.addEventListener('click', ()=>{
        document.querySelector('#principal').scrollIntoView({behavior:'smooth'});
    });

    

    /* Script que actualiza el año en el footer */
    const actualYear = document.querySelector("#actualYear");
    let year = today.getFullYear();
    actualYear.innerHTML = year;

}