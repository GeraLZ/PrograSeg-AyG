import base64
import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher , algorithms , modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def cifrar(mensaje,llave,iv):
    msj = mensaje.encode('utf-8')
    key = base64.b64decode(llave.encode('utf-8'))
    nonce = base64.b64decode(iv.encode('utf-8'))
    
    aesCipher = Cipher (algorithms.AES(key),
                        modes.CTR(nonce),
                        backend = default_backend())
    
    cifrador = aesCipher.encryptor()
    mensaje_cifrado = cifrador.update(msj)
    cifrador.finalize()
    return base64.b64encode(mensaje_cifrado).decode('utf-8')

def descifrar(mensaje,llave,iv):
    msj = base64.b64decode(mensaje.encode('utf-8'))
    key = base64.b64decode(llave.encode('utf-8'))
    nonce = base64.b64decode(iv.encode('utf-8'))
    
    aesCipher = Cipher (algorithms.AES(key),
                        modes.CTR(nonce),
                        backend = default_backend())
    
    descifrador = aesCipher.decryptor()
    mensaje_descifrado = descifrador.update(msj)
    descifrador.finalize()
    return mensaje_descifrado.decode('utf-8')

def makeIV():
    return base64.b64encode(os.urandom(16)).decode('utf-8')