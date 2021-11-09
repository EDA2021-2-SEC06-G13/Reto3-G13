"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import datetime
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Avistamientos por ciudad")
    print("3- Avistamientos por duración")
    print("4- Avistamientos por Hora/Minutos del día")
    print("5- Avistamientos en un rango de fechas")
    print("6- Avistamientos de una Zona Geográfica")
    

catalog = None


def initCatalog():
    """
    Inicializa el catalogo 
    """
    return controller.initCatalog()

def loadData(catalog):
     return controller.loadData(catalog)


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData(catalog)
        sumatoria=0
        info=om.valueSet(catalog["ufos"])
        for i in range(1,lt.size(info)+1):
            cant_ciudad=lt.getElement(info,i)
            cantidad=lt.size(cant_ciudad)
            sumatoria+=cantidad


        print('Total de UFOS cargados: ' + str(sumatoria))


    elif int(inputs[0]) == 2:
        ciudad=input("Ingrese el nombre de la ciudad: ")
        r=controller.requerimiento_1(ciudad,catalog)
        r_0=r[0]
        r_1=r[1]
        print("Se encontraron "+ str(lt.size(r_0)) +" ciudades con señales UFO")
        print("Hay "+ str(lt.size(r_1))+ " señales en la ciudad: " + ciudad)
        print("Las primeras 3 y ultimas 3 señales UFO son: ")
        for i in range(lt.size(r_1)-6, lt.size(r_1)-3):
            valor=lt.getElement(r_1,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])
        for i in range(5, 8):
            valor=lt.getElement(r_1,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])
    
    elif int(inputs[0])==3:
        limite_inf=input("Ingrese el limite inferior en segundos: ")
        limite_sup= input("Ingrese el limite superior en segundos: ")
        r=controller.requerimiento_2(limite_inf, limite_sup, catalog)
        print("Se encontraron "+str(lt.size(r))+" entre los valores "+str((limite_inf))+" y "+str((limite_sup)))
        print("Las primeras 3 y últimas 3 son: ")
        for i in range(1, 4):
            valor=lt.getElement(r,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])
        for i in range(191, 194):
            valor=lt.getElement(r,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])

    elif int(inputs[0])==4:
        limite_inf=input("Ingrese el limite inferior en formato HH:MM: ")
        limite_sup= input("Ingrese el limite superior en formato HH:MM: ")
        r=controller.requerimiento_3(limite_inf, limite_sup, catalog)
        print("Se encontraron "+str(lt.size(r))+" entre las fechas "+str((limite_inf))+" y "+str((limite_sup)))
        print("Las primeras 3 y últimas 3 son: ")
        for i in range(1, 4):
            valor=lt.getElement(r,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])
        for i in range(lt.size(r)-2,lt.size(r)+1):
            valor=lt.getElement(r,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])
    
    elif int(inputs[0])==5:
        limite_inf=input("Ingrese el limite inferior en formato AAAA-MM-DD: ")
        limite_sup= input("Ingrese el limite superior en formato AAAA-MM-DD: ")
        r=controller.requerimiento_3(limite_inf, limite_sup, catalog)
        print("Hay: "+str(lt.size(r)))
        for i in range(1, 4):
            valor=lt.getElement(r,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])
        for i in range(lt.size(r)-2,lt.size(r)+1):
            valor=lt.getElement(r,i)
            print(valor["datetime"], valor["city"], valor["state"], valor["country"], valor["shape"],valor["duration (seconds)"])


    else:
        sys.exit(0)
sys.exit(0)
