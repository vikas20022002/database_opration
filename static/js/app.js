$(document).ready(function () {
  // $('.car-slider').slick({
  //   infinite: true,
  //   slidesToShow: 1,
  //   slidesToScroll: 1,
  //   arrows: false,
    
  //   responsive: [
  //     {
  //       breakpoint: 769,
  //       settings: {
  //         slidesToShow: 1,
  //         slidesToScroll: 1,
  //       }
  //     },
  //   ]
  // })

  $('.car-slider').slick({
    dots: true,
    infinite: true,
    speed: 500,
    fade: true,
    autoplay: true,
    autoplaySpeed: 1500,
    cssEase: 'linear'
  });
});