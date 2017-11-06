$(function() {
  $('<img/>').attr('src', '../static/img/iconos/inicio.jpg').load(function() {
    $('.bg-img').append($(this));
    // simulate loading  
    $('.container').addClass('loaded');
  });
})
