#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 05/04/2023 4:23pm
#Ultima version:  05/04/2023 5:38pm
#Version: 3.10.6

#Importación de bibliotecas
import re
from funciones import *
    
def ESAnalizarCadena(pPalabra):
    pPalabra=pPalabra.lower()
    if pPalabra!="":
        vocales,consonantes,espacios,numeros,simbolos=analizarCadena(pPalabra)
        return ["Vocales: "+str(vocales),"Consonantes: "+str(consonantes),"Espacios: "+str(espacios),"Numeros: "+str(numeros),"Simbolos: "+str(simbolos)]
    else:
        return "Debe indicar una cadena valida"

#Definición de funciones
def ESGorditoNavidenno():
    """
    Funcionalidad: Muestra el resultado de la función gorditoNavidenno
    Entradas: NA
    Salidas:NA
    """
    for numero in gorditoNavidenno():
        print(numero)

def ESIndicarParidad(pNumero):
    if re.match('^[\d]+$',pNumero):
        return crearLista(int(pNumero))
    return "Debe de ingresar un número"

def validarCarnets(pCarnets):
    """
    Funcionalidad: Valida que los elementos de la lista dada representen carnets
    Entradas:
    -pCarnets(list): Lista de posibles carnets
    Salidas:
    return(bool): True si todos los elementos son carnets válidos, False si no lo son
    """
    for carnet in pCarnets:
        if not re.match("\d{10}", carnet):
            #print("Alguno de los carnets proveídos no es válido (verifque que sean 10 dígitos exactos)")
            return False
    return True

def ESContarGeneraciones(pLista):
    """
    Funcionalidad: Muestra el resultado de la función contarGeneraciones
    Entradas:
    -pLista(list): Lista de carnets a clasificar
    Salidas:NA
    """
    if not validarCarnets(pLista):
        print("Alguno de los carnets proveídos no es válido (verifque que sean 10 dígitos exactos)")
        return
    i = 0
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
    """
    Funcionalidad: Recibe entrada de usuario y muestra un informe de las edades dadas
    Entradas: NA
    Salidas:NA
    """
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

def ESInformeEdadesNoInput(pLista):
    """
    Funcionalidad: Muestra el informe de las edades dadas sin necesitar entrada de datos manual
    Entradas:
    -pLista(list): Lista de edades a analizar
    Salidas:NA
    """
    annoActual = 2023
    menor = encontrarMenor(pLista)
    mayor = encontrarMayor(pLista)

    if esBisiesto(annoActual-mayor):
        bisiesto = "bisiesto"
    else:
        bisiesto = "no bisiesto"
    
    print(f"El menor nació en el año {annoActual-menor} por ende tiene {menor} años\n"
            f"El mayor nació en el año {annoActual-mayor} por ende tiene {mayor} años, esta persona nació en año {bisiesto}\n"
            f"Entre ellos hay {mayor-menor} años de diferencia y entre este rango entonces se encuentran las edades:"
          )
    for i in range(len(pLista)):
        if pLista[i] != menor and pLista[i] != mayor:
            print(f"Edad {i+1}: {pLista[i]}")

#Programa principal
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
print("Entrada: ['2018012344', '2021019876', '2021021234', '2019012345', '2018025678', '2022012345']")
ESContarGeneraciones(["2018012344", "2021019876", "2021021234", "2019012345", "2018025678", "2022012345"])
print("")

print("Notas imaginarias")
print(ESnotasImaginarias())
print("")

print("Listar palindromos")
print("Entrada: ['radar', 'oro', 'rajar', 'ralla', 'sala', 'somos', 'adolfo']")
print(listaPalindromos(["radar", "oro", "rajar", "ralla", "sala", "somos", "adolfo"]))
print("")

print("Clasificando edades")
print(clasificandoEdades("7"))
print("")

print("Informe de edades")
ESInformeEdadesNoInput([23,34,45,56,25])
print("")

print("Producto Cartesiano")
print(ESProductoCartesiano([1,2],["x","y","z"]))
print(ESProductoCartesiano([1,2,3,4],["a","b"]))



