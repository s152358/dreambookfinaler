$(document).ready(function(){

  $('.post').hover(
    function(){
        $(this).fadeTo(500, 0.7);
    },
    function(){
        $(this).fadeTo(500, 1.0);
    }
  );
});
