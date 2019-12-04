const espaco = document.querySelector('.div-quem_somos');
const tresPilares = document.querySelector('.tres_pilares');


/*tresPilares.style.marginTop = `${ espaco.offsetHeight -130 }px`;*/

tresPilares.style.marginTop = `${ espaco.offsetHeight -90 }px`;


/* slick teste */

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