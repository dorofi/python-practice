class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

print(car1.display_info())
print(car2.display_info())
# Output:
# 2020 Toyota Corolla
# 2021 Honda Civic 