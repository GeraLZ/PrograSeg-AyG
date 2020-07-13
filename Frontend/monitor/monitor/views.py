from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from django.shortcuts import render, redirect
from monitorPS import models
from monitor import decorador
from monitor import intentos
from monitor import telegram
from monitor import passwords
from monitor import cifrado_CTR
from monitor import verif_ip
import os
import requests
import json
from django.http import HttpResponseRedirect 
import logging

logging.basicConfig(filename='login.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)

def inicioSesionAdmin(request):
    t = 'inicioSesionAdmin.html'
    if request.method == 'GET':
        request.session.flush() #Borrar la sesion por si existiera algo 
        if request.session.get('logueado') == True:
            return redirect('/paginaInicioAdmin/')
        else:
            return render(request, t) 
    if request.method == 'POST':
        if intentos.dejar_pasar_peticion_login(request):
            usuario = request.POST.get('usuario').strip()
            password = request.POST.get('password').strip()
            
        if models.admin.objects.filter(usuario=usuario).exists():
            getData = models.admin.objects.get(usuario=usuario)
            salt = getData.salt
            hash_pass = getData.password
            if passwords.verificarPass(password,salt,hash_pass):

                setData = models.admin.objects.filter(usuario=usuario)
                setData.update(codigo_token=telegram.tokenTelegram())

                getData = models.admin.objects.get(usuario=usuario)

                telegram.sendToken(getData.id_token, getData.id_chat, getData.codigo_token)
                   
                request.session['logueado'] = True
                request.session.set_expiry(1800)#Tiempo maximo de sesion en segundos, desde que inicio solo se le permitira usar el sistema por X minutos
                     
                return render(request, 'tokenAdmin.html',{'saludo': 'Admin', 'usuario' : getData.usuario}) 
            else:
                c = {'errores': 'Password inválido'}
                return render(request, t, c)
        else:
            c = {'errores': 'Usuario inválido'}
            return render(request, t, c)
    else:
        logging.warning('Intento de login en Administrador Global por Anon')
        return render(request, t, {'errores': 'Demasiados intentos fallidos'})

@decorador.verificar_Admin
def paginaInicioAdmin(request):
    t = 'paginaInicioAdmin.html'   
    c = {'saludo': 'Admin'}
    if request.method == 'GET':
        return render(request, t)
    if request.method == 'POST':
        usuario = request.POST.get('usuario').strip()
        tokenT = request.POST.get('token').strip()
        if models.admin.objects.filter(usuario=usuario,codigo_token=tokenT).exists():
            models.admin.objects.filter(usuario=usuario,codigo_token=tokenT).update(codigo_token=None)
            logging.info('Se ha logueado el usuario %s',usuario)
            return render(request, t, c)
        else:
            request.session['logueado'] = False
            return redirect('/inicioSesionAdmin/')

@decorador.verificar_Admin
def listarUser(request):
    t = 'lista_usuarios.html'
    usuarios = models.user.objects.all()
    c = {'usuarios': usuarios}
    if request.method == 'GET':
        return render(request, t, c)

@decorador.verificar_Admin
def listarServer(request):
    t = 'lista_servers.html'
    servidores = models.servers.objects.all()
    c = {'servidores': servidores}
    if request.method == 'GET':
        return render(request, t, c)

def asociar(request):
    t = 'asociar.html'
    if request.method == 'GET':
        return render(request, t)
    if request.method == 'POST':
        admin = request.POST.get('admin').strip() #nombre del administracion
        server = request.POST.get('server').strip() #ip del servidor
        if models.user.objects.filter(usuario=admin).exists():
            if models.servers.objects.filter(ip=server).exists():
                setData = models.servers.objects.filter(ip=server)
                setData.update(admin=admin)
                logging.info('Se ha asociado el admnistrador %s con el servidor %s', admin, server)
                return redirect('/listarServer/')
            else:
                c = { 'errores': 'El servidor no existe' }
                return render(request, t, c)
        else:
            c = { 'errores': 'El administrador no existe' }
            return render(request, t, c)

@decorador.verificar_Admin
def registroUser(request):
    t = 'registroUser.html'
    if request.method == 'GET':
        return render(request, t)
    if request.method == 'POST':
        usuario = request.POST.get('usuario', '').strip()
        if models.user.objects.filter(usuario=usuario).exists():
            c = { 'errores': 'El usuario ya esta en uso' }
            t = 'registroUser.html'
            return render(request,t, c)
        
        password = request.POST.get('password', '').strip()
        if passwords.passwordValida(password):
            salt_generada = passwords.makeSalt()
            usuarios = models.user()
            usuarios.usuario = request.POST.get('usuario').strip()
            usuarios.salt = salt_generada
            usuarios.password = passwords.hashearPass(request.POST.get('password').strip(),salt_generada)
            usuarios.id_chat = request.POST.get('id_chat').strip()
            usuarios.id_token = request.POST.get('id_token').strip()
            usuarios.save()
            logging.info('Se ha registrado un usuario %s', usuarios.usuario)
            return redirect('/paginaInicioAdmin/')
        else:
            c = { 'errores': 'La password debe de contener al menos una mayúscula, una minúscula, un número y un carácter especial(@$!#%*?&-_) y tener una longitud mayor a 8 y menor a 20 caracteres' }
            t = 'registroUser.html'
            return render(request,t, c)

@decorador.verificar_Admin
def registroServer(request):
    t = 'registroServer.html'
    if request.method == 'GET':
        return render(request, t)
    if request.method == 'POST':
        ip = request.POST.get('ip', '').strip()
        if verif_ip.ipValida(ip):
    
            if models.servers.objects.filter(ip=ip).exists():
                c = { 'errores': 'La ip ya esta un uso' }
                t = 'registroUser.html'
                return render(request,t, c)

            servidor = models.servers()
            servidor.ip = request.POST.get('ip').strip()
            servidor.api_user = request.POST.get('api_user').strip()
            iv_generada = cifrado_CTR.makeIV()
            servidor.api_iv =iv_generada
            key = os.environ.get('API_PASSWORD')
            servidor.api_password = cifrado_CTR.cifrar(request.POST.get('api_password').strip(),key,iv_generada)
            servidor.save()
            logging.info('Se ha registrado un servidor %s', servidor.ip)
            return redirect('/paginaInicioAdmin/')
        else:
            c = { 'errores': 'La ip no es valida' }
            t = 'registroServer.html'
            return render(request,t, c)

def logout(request):
    #request.session['logueado'] = False
    request.session.flush() #para borrar de la base de datos y de las cookies
    return redirect('/inicioSesionAdmin/')

def inicioSesionUser(request):
    t = 'inicioSesionUser.html'
    if request.method == 'GET':
        request.session.flush() #Borrar la sesion por si existiera algo
        return render(request, t)
    if request.method == 'POST':
        if intentos.dejar_pasar_peticion_login(request):
            usuario = request.POST.get('usuario').strip()
            password = request.POST.get('password').strip()
            
        if models.user.objects.filter(usuario=usuario).exists():
            getData = models.user.objects.get(usuario=usuario)
            salt = getData.salt
            hash_pass = getData.password
            if passwords.verificarPass(password,salt,hash_pass):

                setData = models.user.objects.filter(usuario=usuario)
                setData.update(codigo_token=telegram.tokenTelegram())

                getData = models.user.objects.get(usuario=usuario)

                telegram.sendToken(getData.id_token, getData.id_chat, getData.codigo_token)
                   
                request.session['logueadoUser'] = True
                request.session.set_expiry(900)#Tiempo maximo de sesion en segundos, desde que inicio solo se le permitira usar el sistema por X minutos
                    
                return render(request, 'tokenUser.html',{'saludo': 'User', 'usuario' : getData.usuario}) 
            else:
                c = {'errores': 'Password inválido'}
                return render(request, t, c)
        else:
            c = {'errores': 'Usuario inválido'}
            return render(request, t, c)
    else:
        logging.warning('Intento de login de Usuario por Anon')
        return render(request, t, {'errores': 'Demasiados intentos fallidos'})

@decorador.verificar_Usuario
def paginaInicioUser(request):
    t = 'paginaInicioUser.html'

    if request.method == 'GET':
        admin= request.session['usuario']
        servidores = models.servers.objects.filter(admin=admin)
        c = {'servidores': servidores}
        return render(request, t,c)
        
    if request.method == 'POST':
        usuario = request.POST.get('usuario').strip()
        tokenT = request.POST.get('token').strip()
        if models.user.objects.filter(usuario=usuario,codigo_token=tokenT).exists():
            models.user.objects.filter(usuario=usuario,codigo_token=tokenT).update(codigo_token=None)
            
            servidores = models.servers.objects.filter(admin=usuario)
            request.session['usuario'] = usuario
            c = {'servidores':servidores}
            logging.info('Se ha logueado el usuario %s', usuario)
            return render(request,t,c)
        else:
            request.session['logueadoUser'] = False
            request.session.flush() 
            return redirect('/inicioSesionUser/')

@decorador.verificar_Usuario
def monitorizar(request):
    t = 'monitorizar.html'

    if request.method == 'GET':
        return redirect('/paginaInicioUser/')
    
    if request.method == 'POST':
        ip = request.POST.get('ip').strip()
        key = os.environ.get('API_PASSWORD')
        getData = models.servers.objects.get(ip=ip)

        pswAPI = cifrado_CTR.descifrar(getData.api_password,key,getData.api_iv)
        url = 'http://'+ip+':8000/autenticacion/'
        datos = {'username': getData.api_user, 'password': pswAPI}
        res = requests.post(url,datos)
        
        if res.status_code == 200:
            token_json=json.loads(res.text)
            authtok = token_json['token']
            
            url2 = 'http://'+ip+':8000/datos/'
            head_Tk = { 'Authorization': 'Token ' + authtok}
            
            res2 = requests.get(url2, headers = head_Tk)
            data_json = json.loads(res2.text)
            
            cpuS = data_json[u'cpu']
            discoS = data_json[u'disco']
            memoriaS = data_json[u'memoria']

            c = {'ip': ip, 'memoria': memoriaS, 'cpu': cpuS, 'memoria': memoriaS, 'disco': discoS}
            return render(request,t, c)
        else:
            return redirect('/paginaInicioUser/')


def logoutUser(request):
    #request.session['logueadoUser'] = False
    request.session.flush() #para borrar de la base de datos y de las cookies
    return redirect('/inicioSesionUser/')