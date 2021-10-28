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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    catalog = {'ufos': None}

    catalog['ufos'] = mp.newMap(1000,maptype='PROBING',loadfactor=0.5,comparefunction=cmpufos)
    return catalog



def cmpufos(data,data_entry):

    x = me.getKey(data_entry)    
    if int(data) == int(x):         
        return 0     
    elif int(data) > int(x):         
        return 1     
    else:         
        return -1



def addUfos(catalog,ufo):
    presente = mp.contains(catalog["ufos"], ufo["city"])
    if not presente:
        lista=lt.newList()
        mp.put(catalog["ufos"],ufo["city"],lista)
        nombre=ufo["city"]
        lt.addFirst(catalog["ufos"][nombre],ufo)
    else:
        nombre=ufo["city"]
        lt.addLast(catalog["ufos"][nombre],ufo)





"""""
def primer_requerimiento(nombre_ciudad,catalog):

"""
# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
