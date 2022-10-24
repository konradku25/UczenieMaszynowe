def hello(name: str, surname: str) -> str:
    return ("Cześć {} {}!".format(name, surname))

def isEven(l1):
    wyn = True
    if l1 % 2 != 0:
        wyn = False
    return wyn

def multiply(l1: int, l2: int):
    return (l1 * l2)

def compare(l1: int, l2: int, l3: int):
    if l1 + l2 >= 3:
        return True
    else:
        return False

def isIn(lista: list, x: int):
    if x in lista:
        return True
    else:
        return False

def listAppDel3(l1: list, l2: list):
    for x in l2:
        l1.append(x)
    wynik = set(l1)
    wynik = list(wynik)
    for x in range(0, len(wynik)):
        wynik[x] = wynik[x] ** 3
    return wynik