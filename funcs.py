def Zadanie2a(lista):
    for x in lista:
        print(x)

def Zadanie2bI(lista):
    for x in range(0, len(lista)):
        lista[x] = lista[x] * 2
    return lista

def Zadanie2bII(lista):
    lista = [2 * x for x in lista]
    return lista

def Zadanie2c(lista):
    for x in lista:
        if x % 2 == 0:
            if x != 0:
                print(x)

def Zadanie2d(lista):
    for x in range(0, len(lista), 2):
        print(x)
