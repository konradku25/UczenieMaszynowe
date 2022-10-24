# Zadanie 2
import classes.z2 as cl

Biblioteka1 = cl.Library('Rybnik', 'Klasztorna', '44-200', '10-20', '600 300 500')
Biblioteka2 = cl.Library('Zory', 'Francuska', '44-240', '8-16', '599 743 582')

Ksiazka1 = cl.Book(Biblioteka1, '25-10-2008', 'James', 'Hammond', 445)
Ksiazka2 = cl.Book(Biblioteka1, '7-3-1964', 'Aaron', 'Cravitz', 159)
Ksiazka3 = cl.Book(Biblioteka1, '5-12-2021', 'Martin', 'Brundle', 321)
Ksiazka4 = cl.Book(Biblioteka2, '5-5-1955', 'Karun', 'Chandok', 71)
Ksiazka5 = cl.Book(Biblioteka2, '4-9-1997', 'Jamie', 'Chadwick', 754)

Prac1 = cl.Employee("Anthony", "Croft", "21-12-2004", "6-7-1987", "Katowice", "Adamskiego", "40-200", "650 054 124")
Prac2 = cl.Employee("Jack", "Davidson", "12-7-2000", "4-7-1997", "Zabrze", "Przejazdowa", "42-200", "650 477 659")

Zam1 = cl.Order(Prac1, "Student 1", [Ksiazka1, Ksiazka2], "17-10-2022")
print(Zam1)
