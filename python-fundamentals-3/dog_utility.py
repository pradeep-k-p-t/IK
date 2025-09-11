class Dog: 
    def __init__(self, name : str, age : int):
        self.name = name 
        self.age = age 

    # Functions are actions performed by the class 
    def bark(self):
        print(f"{self.name} is barking woof")

    

d = Dog(name="parker",age=4)
d.bark()