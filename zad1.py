import func as f

# Zadanie 1
wynik = f.hello("Konrad", "Kula")
print(wynik)

# Zadanie 2
print(f.multiply(3, 7))

# Zadanie 3
wynik = f.isEven(3)
if wynik:
    print("Liczba Parzysta")
else:
    print("Liczba nieparzysta")

# Zadanie 4
print(f.compare(1, 4, 2))

# Zadanie 5
lista = [14, 31, 11, 23, 44]
print(f.isIn(lista, 8))

# Zadanie 6
lista1 = [1, 2, 4, 5, 6, 7]
lista2 = [2, 5, 3, 8]
print(f.listAppDel3(lista1, lista2))
