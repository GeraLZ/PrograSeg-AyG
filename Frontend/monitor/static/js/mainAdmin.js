$(document).ready(function() {
    // barra de navegacion
    $(".home").click(function() {
        window.location.replace("/paginaInicioAdmin/");
    });

    $(".asociar").click(function() {
        window.location.replace("/asociar/");
    });

    $(".del_server").click(function() {
        window.location.replace("/borrarServer/");
    });

    $(".del_admin").click(function() {
        window.location.replace("/borrarAdmin/");
    });

    $(".salir").click(function() {
        window.location.replace("/logout/");
    });

    //botones pagina de inicio
    $("#registro_admin").click(function() {
        window.location.replace("/registroUser/");
    });

    $("#registro_server").click(function() {
        window.location.replace("/registroServer/");
    });

    $("#lista_admin").click(function() {
        window.location.replace("/listarUser/");
    });

    $("#lista_server").click(function() {
        window.location.replace("/listarServer/");
    });
});