$(document).ready(function() {
    // barra de navegacion
    $(".home").click(function() {
        window.location.replace("/paginaInicioAdmin/");
    });

    $(".asociar").click(function() {
        window.location.replace("/asociar/");
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