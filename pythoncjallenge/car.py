# car.py

class Car:
    def __init__(self, make, model, year):
        # Initialize the Car object with make, model, and year attributes
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Prints the car's information
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
