from django.db import models
import os
import base64

# Create your models here.
class admin(models.Model):
    usuario = models.CharField(max_length=15, default=None)
    password = models.CharField(max_length=100, default=None)
    salt = models.CharField(max_length=25, default=(base64.b64encode(os.urandom(16))).decode('utf-8'))
    id_token = models.CharField(max_length=50, default=None)
    id_chat = models.CharField(max_length=10, default=None)
    codigo_token = models.CharField(max_length=25, default=None)

class ips(models.Model):
    ip = models.GenericIPAddressField(null=False, blank=False, unique=True)
    ultima_peticion = models.DateTimeField(null=False, blank=False)
    intentos = models.IntegerField(null=False, blank=False, default=0)