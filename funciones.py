import random

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

def gorditoNavidenno():
    numeros = []
    while len(numeros)<5:
        aleatorio = random.randint(0,99)
        if aleatorio%2==0:
            numeros.append(aleatorio)
    return numeros

def contarGeneraciones(pLista):
    cuenta = [0,0,0,0,0]
    for carnet in pLista:
        anno= int(carnet[:4])
        cuenta[anno-2018] += 1
    return cuenta

def listaPalindromos(pLista):
    palindromos = []
    for palabra in pLista:
        if palabra == palabra[::-1]:
            palindromos.append(palabra)
    return palindromos

def encontrarMenor(pEdades):
    menor = 1000
    for edad in pEdades:
        if edad<menor:
            menor = edad
    return menor

def encontrarMayor(pEdades):
    mayor = 0
    for edad in pEdades:
        if edad>mayor:
            mayor = edad
    return mayor

def esBisiesto(pAnno):
    return pAnno % 4 == 0 and (pAnno % 100 != 0 or pAnno % 400 == 0)