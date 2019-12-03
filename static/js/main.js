const espaco = document.querySelector('.div-quem_somos');
const tresPilares = document.querySelector('.tres_pilares');


/*tresPilares.style.marginTop = `${ espaco.offsetHeight -130 }px`;*/

tresPilares.style.marginTop = `${ espaco.offsetHeight -90 }px`;


/* slick teste */

$('.carrocel').slick({
    dots: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 3,
    variableWidth: true
});

if (Event.pageX <= 930){
   /* $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
      });
    $('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    dots: true,
    centerMode: true,
    focusOnSelect: true
    });*/
    console.log('mobile');
}


