﻿"""
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

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
        info=mp.valueSet(catalog["ufos"])
        for i in range(1,lt.size(info)+1):
            cant_ciudad=lt.getElement(info,i)
            cantidad=lt.size(cant_ciudad)
            sumatoria+=cantidad


        print('Total de UFOS cargados: ' + str(cantidad))


    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
