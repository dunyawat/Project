$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        loop:true,
        responsive:{
            0:{
                items:1,
                nav:false
            },
            600:{
                items:2,
                nav:false
            },
            1000:{
                items:2,
                nav:true,
                loop:false
            }
        }
    });
  });


$('.to-top').click(function(){
    $('html, body').animate({scrollTop:'0px'},400)
})
