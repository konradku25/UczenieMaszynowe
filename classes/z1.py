class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_Passed(self):
        if self.marks > 50:
            return True
        else:
            return False
