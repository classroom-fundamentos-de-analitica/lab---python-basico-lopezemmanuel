"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01():
    suma = 0

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            suma += int(fila[1])

    return suma


def pregunta_02():
    letras = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            letras.append(fila[0])
    
    salida = []
    
    for letra in sorted(set(letras)):
        salida.append((letra, letras.count(letra)))

    return salida


def pregunta_03():
    letras = []
    conteo = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if not fila[0] in letras:
                letras.append(fila[0])
                conteo.append(int(fila[1]))
            else:
                conteo[letras.index(fila[0])] += int(fila[1])

    salida = []
    
    for letra in sorted(letras):
        salida.append((letra, conteo[letras.index(letra)]))

    return salida

def pregunta_04():
    meses = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            mes = fila[2].split('-')[1]
            meses.append(mes)

    salida = []

    for mes in sorted(set(meses)):
        salida.append((mes, meses.count(mes)))

    return salida
    
def pregunta_05():
    letras = []
    conteo = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if not fila[0] in letras:
                letras.append(fila[0])
                conteo.append([int(fila[1])])
            else:
                conteo[letras.index(fila[0])].append(int(fila[1]))

    salida = []

    for letra in sorted(set(letras)):
        salida.append((letra, max(conteo[letras.index(letra)]), min(conteo[letras.index(letra)])))
    
    return salida

print(pregunta_05())

def pregunta_06():
    cadenas = []
    valores = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            diccionario = fila[4].split(',')

            for elemento in diccionario: 
                cadena = elemento.split(':')[0]
                valor = elemento.split(':')[1]

                if cadena not in cadenas:
                    cadenas.append(cadena)
                    valores.append([int(valor)])
                else:
                    valores[cadenas.index(cadena)].append(int(valor))

    salida = []

    for cadena in sorted(cadenas):
        salida.append((cadena, min(valores[cadenas.index(cadena)]), max(valores[cadenas.index(cadena)])))

    return salida

# def pregunta_07():
#     """
#     Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
#     valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
#     a dicho valor de la columna 2.

#     Rta/
#     [
#         (0, ["C"]),
#         (1, ["E", "B", "E"]),
#         (2, ["A", "E"]),
#         (3, ["A", "B", "D", "E", "E", "D"]),
#         (4, ["E", "B"]),
#         (5, ["B", "C", "D", "D", "E", "E", "E"]),
#         (6, ["C", "E", "A", "B"]),
#         (7, ["A", "C", "E", "D"]),
#         (8, ["E", "D", "E", "A", "B"]),
#         (9, ["A", "B", "E", "A", "A", "C"]),
#     ]

#     """
#     return


# def pregunta_08():
#     """
#     Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
#     de la segunda columna; la segunda parte de la tupla es una lista con las letras
#     (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
#     valor de la segunda columna.

#     Rta/
#     [
#         (0, ["C"]),
#         (1, ["B", "E"]),
#         (2, ["A", "E"]),
#         (3, ["A", "B", "D", "E"]),
#         (4, ["B", "E"]),
#         (5, ["B", "C", "D", "E"]),
#         (6, ["A", "B", "C", "E"]),
#         (7, ["A", "C", "D", "E"]),
#         (8, ["A", "B", "D", "E"]),
#         (9, ["A", "B", "C", "E"]),
#     ]

#     """
#     return


# def pregunta_09():
#     """
#     Retorne un diccionario que contenga la cantidad de registros en que aparece cada
#     clave de la columna 5.

#     Rta/
#     {
#         "aaa": 13,
#         "bbb": 16,
#         "ccc": 23,
#         "ddd": 23,
#         "eee": 15,
#         "fff": 20,
#         "ggg": 13,
#         "hhh": 16,
#         "iii": 18,
#         "jjj": 18,
#     }

#     """
#     return


# def pregunta_10():
#     """
#     Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
#     cantidad de elementos de las columnas 4 y 5.

#     Rta/
#     [
#         ("E", 3, 5),
#         ("A", 3, 4),
#         ("B", 4, 4),
#         ...
#         ("C", 4, 3),
#         ("E", 2, 3),
#         ("E", 3, 3),
#     ]


#     """
#     return


# def pregunta_11():
#     """
#     Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
#     columna 4, ordenadas alfabeticamente.

#     Rta/
#     {
#         "a": 122,
#         "b": 49,
#         "c": 91,
#         "d": 73,
#         "e": 86,
#         "f": 134,
#         "g": 35,
#     }


#     """
#     return


# def pregunta_12():
#     """
#     Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
#     los valores de la columna 5 sobre todo el archivo.

#     Rta/
#     {
#         'A': 177,
#         'B': 187,
#         'C': 114,
#         'D': 136,
#         'E': 324
#     }

#     """
#     return
