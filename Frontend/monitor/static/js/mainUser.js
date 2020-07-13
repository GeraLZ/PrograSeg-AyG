$(document).ready(function() {
    // barra de navegacion
    $(".home").click(function() {
        window.location.replace("/paginaInicioUser/");
    });

    $(".salir").click(function() {
        window.location.replace("/logoutUser/");
    });

    $("#monitor").click(function() {
        window.location.replace("/monitorizar/");
    });

    //$("#ttyd").click(function() {
    //    window.location.replace("/listarServerUser/");
    //});
});