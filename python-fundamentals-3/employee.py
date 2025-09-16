class Employee:
    def __init__(self,id,age):
        self.id=id
        self.age=age
    
    def printDetails(self):
        print(self.id)
        print(self.age)
    
    def printAge(abc):
        print(abc.age)

emp1=Employee('E001',25)
emp1.printDetails()
emp1.age = 30
emp1.printDetails()
emp1.printAge()