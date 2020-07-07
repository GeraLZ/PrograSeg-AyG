from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from django.shortcuts import render, redirect
from monitorPS import models
from monitor import decorador
from monitor import intentos
from monitor import telegram
from monitor import passwords

from django.http import HttpResponseRedirect 


def inicioSesionAdmin(request):
    t = 'inicioSesionAdmin.html'
    if request.method == 'GET':
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
                    
                return render(request, 'tokenAdmin.html',{'saludo': 'Admin', 'usuario' : getData.usuario}) 
            else:
                c = {'errores': 'Password inválido'}
                return render(request, t, c)
        else:
            c = {'errores': 'Usuario inválido'}
            return render(request, t, c)
    else:
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
            return render(request, t, c)
        else:
            request.session['logueado'] = False
            return redirect('/inicioSesionAdmin/')

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

def logout(request):
    request.session['logueado'] = False
    #request.session['logueadoClient'] = False
    return redirect('/inicioSesionAdmin/')

def inicioSesionUser(request):
    t = 'inicioSesionUser.html'
    if request.method == 'GET':
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
                    
                return render(request, 'tokenUser.html',{'saludo': 'User', 'usuario' : getData.usuario}) 
            else:
                c = {'errores': 'Password inválido'}
                return render(request, t, c)
        else:
            c = {'errores': 'Usuario inválido'}
            return render(request, t, c)
    else:
        return render(request, t, {'errores': 'Demasiados intentos fallidos'})

@decorador.verificar_Usuario
def paginaInicioUser(request):
    t = 'paginaInicioUser.html'
    c = {'saludo': 'Admin'}
    if request.method == 'GET':
        return render(request, t)
    if request.method == 'POST':
        usuario = request.POST.get('usuario').strip()
        tokenT = request.POST.get('token').strip()
        if models.user.objects.filter(usuario=usuario,codigo_token=tokenT).exists():
            models.user.objects.filter(usuario=usuario,codigo_token=tokenT).update(codigo_token=None)
            return render(request, t, c)
        else:
            request.session['logueadoUser'] = False
            return redirect('/inicioSesionUser/')

def logoutUser(request):
    request.session['logueadoUser'] = False
    return redirect('/inicioSesionUser/')