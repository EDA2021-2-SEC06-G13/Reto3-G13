"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.ADT import orderedmap as om
import datetime
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    catalog = {'ufos': None}

    catalog['ufos'] = om.newMap('BST',comparefunction=cmpufos)
    return catalog



def cmpufos(city_1,city_2):  
    if city_1 == city_2:         
        return 0     
    elif city_1 > city_2:         
        return 1     
    else:         
        return -1
def cmpfunction(uno,dos):

    if int(uno["duration (seconds)"])> int(dos["duration (seconds)"]):
        r=True
    else:
        r=False
    return r



def addUfos(catalog,ufo):
    presente = om.contains(catalog["ufos"], ufo["city"])
    if not presente:
        lista=lt.newList()
        lt.addFirst(lista, ufo)
        om.put(catalog["ufos"],ufo["city"],lista)
        
    else:
        nombre=ufo["city"]
        entry = om.get(catalog["ufos"], nombre)
        lista=me.getValue(entry)
        lt.addLast(lista, ufo)




def primer_requerimiento(nombre_ciudad,catalog):
    lista=om.keySet(catalog["ufos"])
    if om.contains(catalog["ufos"],nombre_ciudad):
        entry=om.get(catalog["ufos"], nombre_ciudad)
        value= me.getValue(entry)
    return(lista,value)


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
