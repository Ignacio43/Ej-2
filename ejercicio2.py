from clases import ViajeroFrecuente
import funciones2

if __name__=='__main__':
    menu=-1
    p=[]
    p=listadeviajeros()
    
    menu=input(print("0: salir \n1: mostrar cantidad total de millas \n2:acumular millas \n3:canjear millas \n"))
    while menu != 0:
        numero_viaje=input("ingrese el numero del viajero ")
        viajero=confirmacionViajero(p,numero_viaje)

        if viajero.get_num_viaje() == numero_viaje:     #type(str)
            if menu ==1:
                print(f"la cantidad total de millas es de {viajero.cantidadTotalMillas()} \n")
            elif menu ==2:
                numero_millas=input("numero de millas")
                print(f"el numero total de millas acumuladas es:{viajero.acumularMillas(numero_millas)} ")
            elif menu ==3:
                millascanje=input("ingrese las millas a canjear")
                print(f"{viajero.canjearMillas(millascanje)} la cantidad de millas actuales pasa a ser {viajero.cantidadTotalMillas()} ")
        else:
            print("el viajero no es un viajero frecuente")
        menu=input(print("0: salir \n1: mostrar cantidad total de millas \n2:acumular millas \n3:canjear millas \n"))


    
    