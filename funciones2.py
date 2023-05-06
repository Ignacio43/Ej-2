import csv
from clases import ViajeroFrecuente

def listadeviajeros():
    listaViajeros=[]
    with open('datos.csv','r')as archivo:
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            viajero=ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
            listaViajeros.append(viajero)  
    
    return(listaViajeros) 

def confirmacionViajero(listaViajeros,numero_viaje):
    bandera=True
    i=0
    while bandera==True and i<len(listaViajeros):
        if listaViajeros[i].get_num_viaje()==numero_viaje: 
           bandera=False
        i+=1
    if i==len(listaViajeros):
        print("no se encontro")
    else:
        return listaViajeros[i]