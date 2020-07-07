from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from django.shortcuts import render, redirect
from monitorPS import models
from monitor import decorador
from monitor import intentos

def inicioSesion(request):
    t = 'inicioSesion.html'
    if request.method == 'GET':
        return render(request, t)
    elif request.method == 'POST':
        if intentos.dejar_pasar_peticion_login(request):
            usuario = request.POST.get('usuario').strip()
            password = request.POST.get('password').strip()
            try:
                models.admin.objects.get(usuario=usuario, password=password)
                return redirect('/paginaInicioAdmin/')
            except:
                c = {'errores': 'Usuario o password inválido'}
                return render(request, t, c)
        else:
            return render(request, t, {'errores': 'Demasiados intentos fallidos'})

#@decorador.verificar_admin
def paginaInicioAdmin(request):
    t = 'hola.html'
    c = {'saludo': 'Admin', 'error': True}
    return render(request, t, c)