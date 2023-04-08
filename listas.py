#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 05/04/2023 4:23pm
#Ultima version:  05/04/2023 5:38pm
#Version: 3.10.6

#Importación de bibliotecas
import re
from funciones import validarEntero, gorditoNavidenno, contarGeneraciones, listaPalindromos, encontrarMenor, encontrarMayor, esBisiesto

#Definición de funciones
def ESGorditoNavidenno():
    """
    Funcionalidad: Muestra el resultado de la función gorditoNavidenno
    Entradas: NA
    Salidas:NA
    """
    for numero in gorditoNavidenno():
        print(numero)

def validarCarnets(pCarnets):
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

def ESInformeEdades():
    """
    Funcionalidad: Recibe entrada de usuario y muestra resultado de InformeEdades
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

#Programa principal
print("Gordito Navideño")
ESGorditoNavidenno()
print("")

print("Contar Generaciones")
print("Entrada: ['2018012344', '2021019876', '2021021234', '2019012345', '2018025678', '2022012345']")
ESContarGeneraciones(["2018012344", "2021019876", "2021021234", "2019012345", "2018025678", "2022012345"])
print("")

print("Listar palindromos")
print("Entrada: ['radar', 'oro', 'rajar', 'ralla', 'sala', 'somos', 'adolfo']")
print(listaPalindromos(["radar", "oro", "rajar", "ralla", "sala", "somos", "adolfo"]))
print("")

print("Informe de edades")
ESInformeEdades()

