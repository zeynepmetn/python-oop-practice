class Vehicle:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year

    def display_info(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}"
class Car(Vehicle):
    def __init__(self, brand, model, year, car_type):
        super().__init__(brand, model, year)
        self.__car_type = car_type

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, car type: {self.__car_type}"

    def special_feature(self):
        return self.__car_type

class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.__load_capacity = load_capacity

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, load capacity: {self.__load_capacity}"

    def special_feature(self):
        return self.__load_capacity

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, cc):
        super().__init__(brand, model, year)
        self.__cc = cc

    def special_feature(self):
        return self.__cc

araba = Car("toyota", "x", 2012, "sedan")
print(araba.display_info())
print(araba.special_feature())

truck = Truck("qwe", "acca", 2000, 123)
print(truck.display_info())
print(truck.special_feature())

motor = Motorcycle("cvb", "cac", 2004, 1000)
print(motor.display_info())
print(motor.special_feature())