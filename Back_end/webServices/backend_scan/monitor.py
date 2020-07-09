import psutil
import platform
from datetime import datetime
import json

def uso_memoria():
    memoria=psutil.virtual_memory().percent
    return memoria

def uso_cpu():
    cpu = psutil.cpu_percent()
    return cpu

def uso_disco():
    particiones =  psutil.disk_partitions()
    for particion in particiones:
        try:
            partition_usage = psutil.disk_usage(particion.mountpoint)
        except PermissionError:
            continue
        disco = partition_usage.percent
        return disco

def uso_discoT():
    discoT= psutil.disk_usage("/").percent
    return discoT

def dataJson():
    uDisco = uso_discoT()
    uMemoria = uso_memoria()
    uCPU = uso_cpu()

    return json.dumps(
        {'disco': uDisco,
         'memoria': uMemoria,
         'cpu': uCPU })
    
if __name__ == '__main__':
    ##print ("="*20 , " USO TOTAL DE MEMORIA ", "="*20, "\n")
    ##print ("Uso total de Memoria: ", uso_memoria(), "%", "\n")

    ##print ("="*20 , " USO TOTAL DE CPU ", "="*20, "\n")    
    ##print ("Uso total de CPU: " ,uso_cpu(), "%", "\n" )

    ##print ("="*20 , " USO TOTAL DE DISCO ", "="*20, "\n")
    ##print ("Uso total de Disco: ", uso_discoT(), "%", "\n")

    ##print ("="*20 , " USO DE DISCO ", "="*20, "\n")
    ##print ("Uso total de disco: " ,uso_disco(), "%", "\n")
	print (dataJson())
