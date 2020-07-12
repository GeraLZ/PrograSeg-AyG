import django
django.setup()
import os

from django.contrib.auth.models import  User
res = User.objects.filter(username=os.environ.get('CLIENTE_SERVICIOS_USR', 'nada'))

if len(res) == 0:
    User.objects.create_user(username=os.environ.get('CLIENTE_SERVICIOS_USR', ''), password=os.environ.get('CLIENTE_SERVICIOS_PWD', ''))