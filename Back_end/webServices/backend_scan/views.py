from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from backend_scan import monitor
import json

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def datos_list(request):
    if request.method =='GET':
        datos_raw = monitor.dataJson()
        datos = json.loads(datos_raw)
        return Response(datos)
# Create your views here.
