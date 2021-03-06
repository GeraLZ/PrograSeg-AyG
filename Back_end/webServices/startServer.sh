#!/bin/bash

function modoUso() {
    echo "Iniciar servidor para monitorizar servidores"
    echo "  startServer.sh archivo.cpt"
    echo "  "
    echo "  Argumentos:"
    echo "      archivo: archivo cifrado donde estan las variables de entorno"
}

function validarParam() {
    #validar que se paso un parametro
        [[ "$1" ]] || { echo "Se necesitan pasar un parametro"; modoUso; exit 1; }
    #validar que se recibio un archivo
    	[[ -f $1 ]] || { echo "El paramentro recibido debe de ser un archivo"; modoUso; exit 1; }
}

validarParam $@

archivo=$1
#ccrypt -d -c $archivo) -> Para conseguir el texto de mi archivo cifrado sin descifrar
for var in $(ccrypt -d -c $archivo); do
    export $var
done

python3 manage.py runserver
#python3 manage.py shell
