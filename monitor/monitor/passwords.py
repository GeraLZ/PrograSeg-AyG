import os
import base64
import crypt
import re

from django.http import HttpResponseRedirect 

def hashearPass(password, salt):  
    return crypt.crypt(password, '$6$' + salt)

def verificarPass(password,salt,password_hash):
    hash_pass = hashearPass(password,salt)
    if hash_pass == password_hash:
        return True
    else:
        return False

def passwordValida(password):
    reg = "^(?=.*[\da-zA-Z@$!#%*?&-_])[A-Za-z\d@$!#%*?&-_]{8,20}$"
    # \d = Coincide con cualquier cifra del 0 al 9 (ambos incluidos).
    # @$!%*#?& = caracteres especiales

    pat = re.compile(reg)
    mat = re.search(pat, password)
    if mat:
        return True
    else:
        return False

def makeSalt():
    return base64.b64encode(os.urandom(16)).decode('utf-8')
