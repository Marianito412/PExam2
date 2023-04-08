#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 05/04/2023 4:23pm
#Ultima version:  05/04/2023 5:38pm
#Version: 3.10.6

#Importación de bibliotecas
import random

#Definición de funciones
def validarEntero(pnumero):
    """
    Funcionalidad: Valida que el valor dado sea un entero positivo
    Entradas:
    -pnumero(str): El valor a validar
    Salidas:
    -pnumero(int): El valor validado si cumple con todos los requisitos
    """
    while True:
        try:
            pnumero = int(pnumero)
            if pnumero >=0:
                break
            else:
                print("Ingrese un valor positivo")
        except ValueError:
            try:
                pnumero = float(pnumero)
                print("El número debe ser entero")
            except ValueError:
                print("Ingrese un valor numérico")
        pnumero = input("Ingrese un número: ")
    return pnumero

def gorditoNavidenno():
    """
    Funcionalidad: Genera 5 números pares aleatorios
    Entradas: NA
    Salidas:
    -numeros(list): La lista de 5 pares aleatorios
    """
    numeros = []
    while len(numeros)<5:
        aleatorio = random.randint(0,99)
        if aleatorio%2==0:
            numeros.append(aleatorio)
    return numeros

def contarGeneraciones(pLista):
    """
    Funcionalidad: Cuenta los miembros de cada generación en una lista de carnets
    Entradas:
    -pLista(list): La lista de carnets a clasificar
    Salidas:
    -cuenta(list): La lista de conteos de cada generación (empezando en 2018)
    """
    cuenta = [0,0,0,0,0]
    for carnet in pLista:
        anno= int(carnet[:4])
        cuenta[anno-2018] += 1
    return cuenta

def listaPalindromos(pLista):
    """
    Funcionalidad: Lista los palíndromos en una lista dada
    Entradas:
    -pLista(list): Lista de palabras
    Salidas:
    -palindromos: Lista de palíndromos contenidos el pLista
    """
    palindromos = []
    for palabra in pLista:
        if palabra == palabra[::-1]:
            palindromos.append(palabra)
    return palindromos

def encontrarMenor(pEdades):
    """
    Funcionalidad: Encuentra el menor valor de una lista dada
    Entradas:
    -pEdades(list): Lista de números en el que desea conocer el menor
    Salidas:
    -menor(int): El menor valor de la lista dada
    """
    menor = 1000
    for edad in pEdades:
        if edad<menor:
            menor = edad
    return menor

def encontrarMayor(pEdades):
    """
    Funcionalidad: Encuentra el mayor valor de una lista dada
    Entradas:
    -pEdades(list): Lista de números en el que desea conocer el mayor
    Salidas:
    -mayor(int): El mayor valor de la lista dada
    """
    mayor = 0
    for edad in pEdades:
        if edad>mayor:
            mayor = edad
    return mayor

def esBisiesto(pAnno):
    """
    Funcionalidad: Verifica si un año dado es bisiesto
    Entradas:
    -pAnno(int): Año que desea clasificar como bisiesto o no bisiesto
    Salidas:
    -return(bool): Verdadero si el año es bisiesto, falso si no lo es 
    """
    return pAnno % 4 == 0 and (pAnno % 100 != 0 or pAnno % 400 == 0)