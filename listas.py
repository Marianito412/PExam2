import re
from funciones import validarEntero, gorditoNavidenno, contarGeneraciones, listaPalindromos, encontrarMenor, encontrarMayor, esBisiesto

def ESGorditoNavidenno():
    for numero in gorditoNavidenno():
        print(numero)

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

print("Gordito Navideño")
ESGorditoNavidenno()
print("")
print("Contar Generaciones")
ESContarGeneraciones(["2018012344", "2021019876", "2021021234", "2019012345", "2018025678", "2022012345"])
print("")
print("Listar palindromos")
print(listaPalindromos(["radar", "oro", "rajar", "ralla", "sala", "somos", "otup"]))
print("")
print("Informe de edades")
ESInformeEdades()

