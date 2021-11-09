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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


def loadData(catalog):
    loadUfos(catalog)


def loadUfos(catalog):
    ufosfile = cf.data_dir + 'UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(ufosfile, encoding='utf-8'))
    for ufo in input_file:
        print(ufo)
        model.addUfos(catalog, ufo)
        model.addUfos_en_hora_minuto(catalog,ufo)
        
        
        
def requerimiento_1(nombre_ciudad,catalog):
    return model.primer_requerimiento(nombre_ciudad,catalog)

def requerimiento_2(limite_inf,limite_sup, catalog):
    return model.segundo_requerimiento(limite_inf, limite_sup, catalog)

def requerimiento_3(limite_inf,limite_sup, catalog):
    return model.tercer_requerimiento(limite_inf, limite_sup, catalog)




# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
