

#Zadanie 3
class Property:
    def __init__(self,area,rooms,price,address):
        self.price = price
        self.area=area
        self.rooms=rooms
        self.price=price
        self.address=address
    def __str__(self):
        return ("Posiadlosc o powierzchni {}, z {} pokojami,o cenie {}, adres: {} ".format(self.area,self.rooms,self.price,self.address))
class House(Property):
    def __init__(self,area,rooms,price,address,plot):
        super().__init__(area,rooms,price,address)
        self.plot=plot
    def __str__(self):
        return ("Dom o powierzchni {}, z dzialka {}, z {} pokojami, o cenie {}, adres: {} ".format(self.area,self.plot,self.rooms,self.price,self.address))
class Flat(Property):
    def __init__(self,area,rooms,price,address,floor):
        super().__init__(area, rooms, price, address)
        self.floor=floor
    def __str__(self):
        return ("Mieszkanie o powierzchni {},na {} pietrze, z {} pokojami, o cenie {}, adres: {} ".format(self.area,self.floor,self.rooms,self.price,self.address))

Dom1 = House('50',7,'700 000','Rybnik ul. Chrobrego 13','80')
print(Dom1)

Dom2 = Flat('25',4,'350 000','Zort ul. 11 Listopada 15',7)
print(Dom2)