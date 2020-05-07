from django.shortcuts import redirect
 
def verificar_admin(vista):
    def interna(request):
        if not request.session.get('logueado', False):
            return redirect('/inicioSesion/')
        return vista(request)
    return interna

def verificar_Usuario(vista):
    def interna(request):
        if not request.session.get('logueadoClient', False):
            return redirect('/inicioSesion/')
        return vista(request)
    return interna