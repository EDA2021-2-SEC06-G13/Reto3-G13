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


from DISClib.DataStructures.arraylist import getElement
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
    catalog["segundos"] = om.newMap('RBT',comparefunction=cmpfunction)
    catalog["latitude"] = om.newMap('RBT',comparefunction=cmpfunction)
    catalog["longitud"] = om.newMap('RBT',comparefunction=cmpfunction)
    catalog["hora-minuto"]= om.newMap('RBT',comparefunction=cmphora_fecha)
    catalog["fecha"]= om.newMap('RBT',comparefunction=cmphora_fecha)
    return catalog



def cmpufos(city_1,city_2):  
    if city_1 == city_2:         
        return 0     
    elif city_1 > city_2:         
        return 1     
    else:         
        return -1
def cmpfunction(uno,dos):
    if float(uno) == float(dos):         
        return 0     
    elif float(uno) > float(dos):         
        return 1     
    else:         
        return -1

def cmpfechas(ufo1,ufo2):
    datetime1=datetime.datetime.strptime(ufo1["datetime"], "%Y-%m-%d %H:%M:%S")
    datetime2=datetime.datetime.strptime(ufo2["datetime"], "%Y-%m-%d %H:%M:%S")
    fecha1=datetime1.date()
    fecha2=datetime2.date()
    return fecha1<fecha2

def less(element1, element2):
    if float(element1["duration (seconds)"]) < float(element2["duration (seconds)"]):
        return True
     

def cmptiempo(tiempo_1,tiempo_2):
    datetime1=datetime.datetime.strptime(tiempo_1["datetime"], "%Y-%m-%d %H:%M:%S")
    datetime2=datetime.datetime.strptime(tiempo_2["datetime"], "%Y-%m-%d %H:%M:%S")
    fecha1=datetime1.time()
    fecha2=datetime2.time()
    return fecha1<fecha2  

def cmphora_fecha(uno,dos):
    if uno==dos:
        return 0
    elif uno>dos:
        return 1
    else:
        return -1

def cmptiempo2(tiempo_1,tiempo_2):
    if tiempo_1==tiempo_2:
        return 0
    elif tiempo_1>tiempo_2:
        return 1
    else:
        return -1
    

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
    segundos=om.contains(catalog["segundos"],ufo["duration (seconds)"])
    if not segundos:
        lista_2=lt.newList()
        lt.addLast(lista_2, ufo)
        om.put(catalog["segundos"], ufo["duration (seconds)"], lista_2)
    else:
        entry = om.get(catalog["segundos"], ufo["duration (seconds)"])
        lista=me.getValue(entry)
        lt.addLast(lista, ufo)
    latitud=om.contains(catalog["latitude"],round(float(ufo["latitude"]),2))
    if not latitud:
        lista_3=lt.newList()
        lt.addLast(lista_3, ufo)
        om.put(catalog["latitude"], round(float(ufo["latitude"]),2), lista_3)
    else:
        entry = om.get(catalog["latitude"], round(float(ufo["latitude"]),2))
        lista=me.getValue(entry)
        lt.addLast(lista, ufo)
    longitud=om.contains(catalog["longitud"],round(float(ufo["longitude"]),2))
    if not longitud:
        lista_4=lt.newList()
        lt.addLast(lista_4, ufo)
        om.put(catalog["longitud"], round(float(ufo["longitude"]),2), lista_4)
    else:
        entry = om.get(catalog["longitud"], round(float(ufo["longitude"]),2))
        lista=me.getValue(entry)
        lt.addLast(lista, ufo)
    
def addUfos_en_hora_minuto(catalog,ufo):
    fecha=datetime.datetime.strptime(ufo["datetime"], "%Y-%m-%d %H:%M:%S")
    hora=fecha.time()
    x=om.contains(catalog["hora-minuto"],(hora))
    if not x:
        lista_2=lt.newList()
        lt.addLast(lista_2, ufo)
        om.put(catalog["hora-minuto"], hora, lista_2)
    else:
        entry = om.get(catalog["hora-minuto"], hora)
        lista=me.getValue(entry)
        lt.addLast(lista, ufo)

def addUfos_en_fecha(catalog,ufo):
    fecha=datetime.datetime.strptime(ufo["datetime"], "%Y-%m-%d %H:%M:%S")
    hora=fecha.date()
    x=om.contains(catalog["fecha"],(hora))
    if not x:
        lista_2=lt.newList()
        lt.addLast(lista_2, ufo)
        om.put(catalog["fecha"], hora, lista_2)
    else:
        entry = om.get(catalog["fecha"], hora)
        lista=me.getValue(entry)
        lt.addLast(lista, ufo)
    
   


def primer_requerimiento(nombre_ciudad,catalog):
    lista=om.keySet(catalog["ufos"])
    if om.contains(catalog["ufos"],nombre_ciudad):
        entry=om.get(catalog["ufos"], nombre_ciudad)
        value= me.getValue(entry)
        value=sa.sort(value,cmpfechas)
    return(lista,value)

def segundo_requerimiento(limite_inf, limite_sup, catalog):
    maximo= om.maxKey(catalog["segundos"])
    lista=om.keys(catalog["segundos"], limite_inf,limite_sup)
    lista_final=lt.newList()
    for i in range(1,lt.size(lista)+1):
        llave=lt.getElement(lista,i)
        entry = om.get(catalog["segundos"], llave)
        lista_2=me.getValue(entry)
        for j in range(1,lt.size(lista_2)+1):
            avistamiento=lt.getElement(lista_2,j)
            lt.addLast(lista_final,avistamiento)
    sa.sort(lista_final,less)
    
    return (maximo,lista_final)


def tercer_requerimiento(limite_inf,limite_sup,catalog):
    limite_inferior=datetime.datetime.strptime(limite_inf, "%H:%M:%S")
    limite_superior=datetime.datetime.strptime(limite_sup, "%H:%M:%S")
    limite_inferior=limite_inferior.time()
    limite_superior=limite_superior.time()

    lista=om.keys(catalog["hora-minuto"], limite_inferior,limite_superior)
    
    lista_final=lt.newList()
    for i in range(1,lt.size(lista)+1):
        llave=lt.getElement(lista,i)
        entry = om.get(catalog["hora-minuto"], llave)
        lista_2=me.getValue(entry)
        for j in range(1,lt.size(lista_2)+1):
            avistamiento=lt.getElement(lista_2,j)
            lt.addLast(lista_final,avistamiento)
    sa.sort(lista_final,cmpfechas)
    
    return lista_final

def cuarto_requerimiento(limite_inf,limite_sup,catalog):
    limite_inferior=datetime.datetime.strptime(limite_inf, "%Y-%m-%d")
    limite_superior=datetime.datetime.strptime(limite_sup, "%Y-%m-%d" )
    limite_inferior=limite_inferior.date()
    limite_superior=limite_superior.date()

    lista=om.keys(catalog["fecha"], limite_inferior,limite_superior)
    
    lista_final=lt.newList()
    for i in range(1,lt.size(lista)+1):
        llave=lt.getElement(lista,i)
        entry = om.get(catalog["fecha"], llave)
        lista_2=me.getValue(entry)
        for j in range(1,lt.size(lista_2)+1):
            avistamiento=lt.getElement(lista_2,j)
            lt.addLast(lista_final,avistamiento)
    sa.sort(lista_final,cmpfechas)
    
    return lista_final


def quinto_requerimiento(longitud_min, longitud_max, latitud_min, latitud_max, catalog):
    lista=om.keys(catalog["latitude"], float(latitud_min), float(latitud_max))
    lista_1=lt.newList()
    for i in range(1,lt.size(lista)+1):
        llave=lt.getElement(lista,i)
        entry = om.get(catalog["latitude"], llave)
        lista_2=me.getValue(entry)
        for j in range(1,lt.size(lista_2)+1):
            avistamiento=lt.getElement(lista_2,j)
            avistamiento["latitude"]=round(float(avistamiento["latitude"]),2)
            avistamiento["longitude"]=round(float(avistamiento["longitude"]),2)
            if avistamiento["longitude"]>=float(longitud_min) and avistamiento["longitude"]<=float(longitud_max): 
                lt.addLast(lista_1,avistamiento)
    return lista_1






# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
