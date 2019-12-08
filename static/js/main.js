const espaco = document.querySelector('.div-quem_somos');
const tresPilares = document.querySelector('.tres_pilares');
const btnHamburguer1 = document.querySelector('.a-1');
const btnHamburguer2 = document.querySelector('.a-2');
const btnHamburguer3 = document.querySelector('.a-3');
const btnHamburguer4 = document.querySelector('.a-4');
const btnHamburguer5 = document.querySelector('.a-5');
const imputHamburguer = document.querySelector('.input-hamburguer');
const sideNav = document.querySelector('.side-nav');

tresPilares.style.marginTop = `${ espaco.clientHeight-50 }px`;

/* slick teste */

btnHamburguer1.addEventListener('click', ()=>{
    imputHamburguer.checked = false;
});
btnHamburguer2.addEventListener('click', ()=>{
    imputHamburguer.checked = false;
});
btnHamburguer3.addEventListener('click', ()=>{
    imputHamburguer.checked = false;
});
btnHamburguer4.addEventListener('click', ()=>{
    imputHamburguer.checked = false;
});
btnHamburguer5.addEventListener('click', ()=>{
    imputHamburguer.checked = false;
});

window.addEventListener('resize',()=>{
    tresPilares.style.marginTop = `${ espaco.clientHeight-50 }px`;

    if ( window.innerWidth <=  930){
    $('.carrocel').slick({
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        variableWidth: true,
        rows: 3
    });
    console.log('if',window.innerWidth);
    }else{
        $('.carrocel').slick({
            dots: true,
            infinite: false,
            slidesToShow: 3,
            slidesToScroll: 3,
            variableWidth: true
        });
        console.log('else');
    }
});

window.addEventListener('load',()=>{
    tresPilares.style.marginTop = `${ espaco.clientHeight-50 }px`;

    if ( window.innerWidth <=  930){
    $('.carrocel').slick({
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        variableWidth: true,
        rows: 3
    });
    
    }else{
        $('.carrocel').slick({
            dots: true,
            infinite: false,
            slidesToShow: 3,
            slidesToScroll: 3,
            variableWidth: true
        });       
    }
});

setInterval(()=>{
    if(window.pageYOffset > 69) {
        sideNav.style.visibility = 'visible';
    }else{
        sideNav.style.visibility = 'hidden';
    }
    
},300);

