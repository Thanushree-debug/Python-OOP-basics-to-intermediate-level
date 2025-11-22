class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def info (self):
        print(f"{self.name} is walking and she is {self.age} years old")
    

c = Human ("Thanu" , 22)

c.info()