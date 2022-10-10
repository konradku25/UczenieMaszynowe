
#Zadanie 2a
imiona=["Sebastian","Esteban","Fernando","Sergio","Nyck"]
def Zadanie2a(lista):
    for x in lista:
        print(x)
Zadanie2a(imiona)


#Zadanie 2b
def Zadanie2bI(lista):
    for x in range(0,len(lista)):
        lista[x]=lista[x]*2
    return lista

liczby=[1,2,3,4,5]
print(Zadanie2bI(liczby))

def Zadanie2bII(lista):
    lista=[2*x for x in lista]
    return lista

print(Zadanie2bII(liczby))

#Zadanie 2c
liczby2=[]
for x in range (0,10):
    liczby2.append(x)

def Zadanie2c(lista):
    for x in lista:
        if x%2==0:
            if x!=0:
                print(x)

Zadanie2c(liczby2)

#Zadanie 2d
def Zadanie2d(lista):
    for x in range(0,len(lista),2):
        print(x)

Zadanie2d(liczby2)












