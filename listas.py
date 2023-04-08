import re
from funciones import *
    
def ESAnalizarCadena(pPalabra):
    pPalabra=pPalabra.lower()
    if pPalabra!="":
        vocales,consonantes,espacios,numeros,simbolos=analizarCadena(pPalabra)
        return ["Vocales: "+str(vocales),"Consonantes: "+str(consonantes),"Espacios: "+str(espacios),"Numeros: "+str(numeros),"Simbolos: "+str(simbolos)]
    else:
        return "Debe indicar una cadena valida"

def ESGorditoNavidenno():
    for numero in gorditoNavidenno():
        print(numero)

def ESIndicarParidad(pNumero):
    if re.match('^[\d]+$',pNumero):
        return crearLista(int(pNumero))
    return "Debe de ingresar un número"

def ESContarGeneraciones(pLista):
    i = 0
    for carnet in pLista:
        if not re.match("\d{10}", carnet):
            print("Alguno de los carnets proveídos no es válido (verifque que sean 10 dígitos exactos)")
            return
    cuenta = contarGeneraciones(pLista)
    while i<len(cuenta):
        print(f"{i+2018}: {cuenta[i]}")
        i+=1

def ESnotasImaginarias():
    aprobados,reposicion,reprobados,promedio,lista=crearListaNotas()
    return "Notas: "+str(lista)+"\nCantidad de aprobados: "+str(aprobados)+"\nCantidad de reposición: "+str(reposicion)+"\nCantidad de reprobados: "+str(reprobados)+ "\nPromedio del grupo: "+str(promedio)

def clasificandoEdades(pNumero):
    if re.match('^[\d]+$',pNumero):
        bebe,niño,adolescente,adultoJoven,adultoMayor,lista=crearListaEdades(int(pNumero))
        return "Edades: "+str(lista)+"\nBebés: "+str(bebe)+"\nNiño: "+str(niño)+"\nAdolescente: "+str(adolescente)+"\nAdulto Joven: "+str(adultoJoven)+ "\nAdulto Mayor: "+str(adultoMayor)
    return "Debe de ingresar un número"

def ESInformeEdades():
    tamanno = validarEntero(input("Cuántas edades desea incluir? "))
    edades = []
    annoActual = 2023
    
    for i in range(tamanno):
        edad = validarEntero(input("Ingrese la edad: "))
        edades.append(edad)
    
    menor = encontrarMenor(edades)
    mayor = encontrarMayor(edades)

    if esBisiesto(annoActual-mayor):
        bisiesto = "bisiesto"
    else:
        bisiesto = "no bisiesto"
    
    print(f"El menor nació en el año {annoActual-menor} por ende tiene {menor} años\n"
            f"El mayor nació en el año {annoActual-mayor} por ende tiene {mayor} años, esta persona nació en año {bisiesto}\n"
            f"Entre ellos hay {mayor-menor} años de diferencia y entre este rango entonces se encuentran las edades:"
          )
    for i in range(len(edades)):
        if edades[i] != menor and edades[i] != mayor:
            print(f"Edad {i+1}: {edades[i]}")

def ESProductoCartesiano(pConjuntos,pLista):
    for i in pConjuntos:
        if not re.match('^[\d*]+$',str(i)):
            return "El primer conjunto debe de ser números"
    for i in pLista:
        if not re.match('^[a-zA-Z*]+$',i):
            return "El segundo conjunto deben de ser letras"
    return productoCartesiano(pConjuntos,pLista)

print("Analizar una cadena de caracteres")
print(ESAnalizarCadena("murcielago"))
print(ESAnalizarCadena(""))
print("")
print("Gordito Navideño")
ESGorditoNavidenno()
print("")
print("Indicando la paridad")
print(ESIndicarParidad("5"))
print("")
print("Contar Generaciones")
ESContarGeneraciones(["2018012344", "2021019876", "2021021234", "2019012345", "2018025678", "2022012345"])
print("")
print("Notas imaginarias")
print(ESnotasImaginarias())
print("")
print("Listar palindromos")
print(listaPalindromos(["radar", "oro", "rajar", "ralla", "sala", "somos", "otup"]))
print("")
print("Clasificando edades")
print(clasificandoEdades("7"))
print("")
print("Informe de edades")
ESInformeEdades()
print("")
print("Producto Cartesiano")
print(ESProductoCartesiano([1,2],["x","y","z"]))
print(ESProductoCartesiano([1,2,3,4],["a","b"]))

