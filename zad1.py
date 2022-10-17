# Zadanie 1
def hello(name: str, surname: str) -> str:
    return ("Cześć {} {}!".format(name, surname))


wynik = hello("Konrad", "Kula")
print(wynik)


# Zadanie 2
def multiply(l1: int, l2: int):
    return (l1 * l2)


print(multiply(3, 7))


# Zadanie 3
def isEven(l1):
    wyn = True
    if l1 % 2 != 0:
        wyn = False
    return wyn


wynik = isEven(3)
if wynik:
    print("Liczba Parzysta")
else:
    print("Liczba nieparzysta")


# Zadanie 4
def compare(l1: int, l2: int, l3: int):
    if l1 + l2 >= 3:
        return True
    else:
        return False


print(compare(1, 4, 2))


# Zadanie 5
def isIn(lista: list, x: int):
    if x in lista:
        return True
    else:
        return False


lista = [14, 31, 11, 23, 44]
print(isIn(lista, 8))


# Zadanie 6
def listAppDel3(l1: list, l2: list):
    for x in l2:
        l1.append(x)
    wynik = set(l1)
    wynik = list(wynik)
    for x in range(0, len(wynik)):
        wynik[x] = wynik[x] ** 3
    return wynik


lista1 = [1, 2, 4, 5, 6, 7]
lista2 = [2, 5, 3, 8]
print(listAppDel3(lista1, lista2))
