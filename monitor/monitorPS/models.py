from django.db import models
import os
import base64

# Create your models here.
class admin(models.Model):
    usuario = models.CharField(max_length=15, default=None)
    password = models.CharField(max_length=110, default=None)
    salt = models.CharField(max_length=25, default=None)
    id_token = models.CharField(max_length=50, default=None)
    id_chat = models.CharField(max_length=10, default=None)
    codigo_token = models.CharField(max_length=25, default=None,blank=True,null=True)

class ips(models.Model):
    ip = models.GenericIPAddressField(null=False, blank=False, unique=True)
    ultima_peticion = models.DateTimeField(null=False, blank=False)
    intentos = models.IntegerField(null=False, blank=False, default=0)

class user(models.Model):
    usuario = models.CharField(max_length=15, default=None)
    password = models.CharField(max_length=110, default=None)
    salt = models.CharField(max_length=25, default=None)
    id_token = models.CharField(max_length=50, default=None)
    id_chat = models.CharField(max_length=10, default=None)
    codigo_token = models.CharField(max_length=25, default=None,blank=True,null=True)