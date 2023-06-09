#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 05/04/2023 4:23pm
#Ultima version:  08/04/2023 6:18pm
#Version: 3.10.6

#Importación de bibliotecas
import random
import re

#Definición de funciones
def analizarCadena(pPalabra):
    """
    Funcionalidad: Cuenta cuantos caracteres hay de cada tipo
    Entradas:
    -pPalabra(str): cadena de caracteres a analizar
    Salidas:
    -vocales,consonantes,espacios,numeros,simbolos(int): Número de caracteres en cada categoría
    """
    pPalabra=pPalabra.lower()
    vocales=len(re.findall('[aeiouáéíóú]',pPalabra))
    consonantes=len(re.findall('[bcdfghjklmnñpqrstvwxyz]',pPalabra))
    espacios=len(re.findall('[\s]',pPalabra))
    numeros=len(re.findall('[\d]',pPalabra))
    simbolos=len(re.findall('[,.;:?!]',pPalabra))
    return vocales,consonantes,espacios,numeros,simbolos

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

def modificarLista(pLista):
    """
    Funcionalidad: Modifica la lista segun si el valor es par o impar
    Entradas:
    -pLista(int): lista de valores aleatorios
    Salidas:
    -pLista(list): lista modificada con un 0 si es par y un 1 si es impar
    """
    for i in range(len(pLista)):
        if esPar(pLista[i]):
            pLista[i]=0
        else:
            pLista[i]=1
    return pLista
        
def crearLista(pNumero):
    """
    Funcionalidad: Crea una lista de numeros aleatorios con la cantidad de pNumero
    Entradas:
    -pNumero(int): numero de valores en la lista
    Salidas:
    -return: Envia la lista a la función modificarLista
    """
    lista=[]
    for i in range(pNumero):
        lista+=[random.randint(0,99)]
    print(lista)
    return modificarLista(lista)

def esPar(pNumero):
    """
    Funcionalidad: comprobar si el valor es par o impar
    Entradas:
    -pNumero(int): valor a analizar
    Salidas:
    -return(bool): True si es par, False si es impar
    """
    
    if pNumero%2==0:
        return True
    return False

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

def clasificarNotas(pLista):
    """
    Funcionalidad: Clasifica los valores de una lista según rangos
    Entradas:
    -pLista(int): lista de valores aleatorios
    Salidas:
    -aprobados,reposicion,reprobados,promedio,pLista(int): Número de valores en cada categoría
    """
    aprobados,reposicion,reprobados,promedio=0,0,0,0
    for i in pLista:
        if i>70:
            aprobados+=1
        elif i>60:
            reposicion+=1
        else:
            reprobados+=1
        promedio+=i
    promedio=promedio/len(pLista)
    return aprobados,reposicion,reprobados,promedio,pLista
            
def crearListaNotas():
    """
    Funcionalidad: Crea una lista de 10 numeros aleatorios
    Salidas:
    -return: Envia la lista a la función clasificarNotas
    """
    lista=[]
    for i in range(10):
        lista+=[random.randint(1,99)]
    return clasificarNotas(lista)

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

def clasificarEdades(pLista):
    """
    Funcionalidad: Clasifica los valores de una lista según rangos
    Entradas:
    -pLista(int): lista de valores aleatorios
    Salidas:
    -bebe,niño,adolescente,adultoJoven,adultoMayor,pLista(int): Número de valores en cada categoría
    """
    bebe,niño,adolescente,adultoJoven,adultoMayor=0,0,0,0,0
    for i in pLista:
        if i>60:
            adultoMayor+=1
        elif i>21:
            adultoJoven+=1
        elif i>12:
            adolescente+=1
        elif i>3:
            niño+=1
        else:
            bebe+=1
    return bebe,niño,adolescente,adultoJoven,adultoMayor,pLista
            
def crearListaEdades(pNumero):
    """
    Funcionalidad: Crea una lista de numeros aleatorios con la cantidad de pNumero
    Entradas:
    -pNumero(int): numero de valores en la lista
    Salidas:
    -return: Envia la lista a la función clasificarEdades
    """
    lista=[]
    for i in range(pNumero):
        lista+=[random.randint(1,99)]
    return clasificarEdades(lista)

def validarEntero(pnumero):
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

def productoCartesiano(pConjuntos,pLista):
    """
    Funcionalidad: retornar todos los posibles pares ordenados de la primera lista con la segunda
    Entradas:
    -pConjuntos(list): primera lista
    -pLista(list): segunda lista
    Salidas:
    -producto(list): todos los posibles pares ordenados
    """
    producto=[]
    for a in pConjuntos:
        for i in pLista:
            producto+=[[a,i]]
    return producto
