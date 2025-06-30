class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(f"name: {self.name}, Roll:{self.roll}")
s1=Student("sneha",11)
s1.display()