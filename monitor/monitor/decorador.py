from django.shortcuts import redirect
 
def verificar_Admin(vista):
    def interna(request):
        if not request.session.get('logueado', False):
            return redirect('/inicioSesionAdmin/')
        return vista(request)
    return interna

def verificar_Usuario(vista):
    def interna(request):
        if not request.session.get('logueadoUser', False):
            return redirect('/inicioSesionUser/')
        return vista(request)
    return interna

def verificar_login(vista):
    def interna(request):
        if request.session.get('logueado') == True:
            return redirect('/paginaInicioAdmin/')
        return vista(request)
    return interna