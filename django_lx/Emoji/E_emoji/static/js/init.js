(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space
$(document).ready(function() {
    $('#makeit').click(function() {
        var one = $("#whoiam").val();
        var two = $("#name").val();
        var three = $("#whatwewant").val();
        var four = $("#idontknow").val();
        var five = $("#when").val();
        var six = $("#now").val();
        $.get("/makeit", {
            'whoiam': one,
            'name': two,
            'whatwewant': three,
            'idontknow': four,
            'when': five,
            'now': six,
        }, function(rec) {
            var img = "data:image/png;base64," + rec;
            $("#result").attr("src", img)
        })
    })
})