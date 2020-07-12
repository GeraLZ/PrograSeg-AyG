$(document).ready(function() {
    // verificar que solo se ingresen los caracteres correctos en el input de la direccion IP
    document.getElementById("ip").addEventListener("input", function() {
        var x = document.getElementById("ip").value;
        var numeros = "0123456789.";
        var ultimo = x.slice(-1);

        if (numeros.indexOf(ultimo) == -1) {
            var erroresJ = document.getElementById("erroresJ");
            /*alert("La ip no es válida")*/
            erroresJ.style.display = "block";
            erroresJ.innerHTML = "<strong>ERROR! </strong>No se permiten estos caracteres";
            document.getElementById("ip").value = x.slice(0, x.length - 1);
        } else {
            var errores = document.getElementById("erroresJ");
            errores.innerHTML = "";
            errores.style.display = (errores.style.display == 'none') ? block : 'none';
        }
    });
});