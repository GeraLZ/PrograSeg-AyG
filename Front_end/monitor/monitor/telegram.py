import requests
import os
import base64
from django.http import HttpResponseRedirect 

def tokenTelegram():
    token=base64.b64encode(os.urandom(16)).decode('utf-8')
    newtoken=''
    for caract in token:
        if caract == '+' or caract =='&':
            newtoken += '0'
        else:
            newtoken += caract

    return newtoken

def sendToken(bot_token, bot_id, bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_id + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)