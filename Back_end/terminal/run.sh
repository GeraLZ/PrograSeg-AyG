#!/bin/bash

su -c "ttyd -c $USER_TTYD:$PASS_TTYD bash" limitado

# $USER:$PASS variables de entorno