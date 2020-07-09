$(document).ready(function() {
    // barra de navegacion
    $(".home").click(function() {
        window.location.replace("/paginaInicioAdmin/");
    });

    $(".registrarUser").click(function() {
        window.location.replace("/registroUser/");
    });

    $(".registrarServer").click(function() {
        window.location.replace("/registroServer/");
    });

    $(".salir").click(function() {
        window.location.replace("/logout/");
    });
});