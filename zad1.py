

#Zadanie 1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_Passed(self):
        if self.marks>50:
            return True
        else:
            return False

stud1 = Student('Bob',51)
print(stud1.is_Passed())
stud2 = Student('Jamie',36)
print(stud2.is_Passed())