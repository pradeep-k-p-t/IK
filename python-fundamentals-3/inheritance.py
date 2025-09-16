class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def print_details(self): 
        print(f"brand name = {self.brand} and model = {self.model}")

class ElectricCars(Car): 

    def __init__(self, brand, model,battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def access_data(self):
        print(f"brand name = {self.brand} and model = {self.model}")
        print(self.battery_capacity)

car1 = Car("mazda","3")
car1.print_details()
electric_car_1 = ElectricCars("mazda","3",5.0)
electric_car_1.access_data()