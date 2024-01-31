# SchneiderHunter_M03_CaseStudy.py
# by Hunter Schneider
# This program allows the user to input information about a car model, then it will display this information
# in an understandable and easy to read format.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.year = ''
        self.make = ''
        self.model = ''
        self.doors = ''
        self.roof = ''

    def get_input(self):
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the type of roof (solid or sun roof): ")

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


# create an instance of the automobile class
car = Automobile("car")

# getting the user input for the car
car.get_input()

# calls the function for displaying car info
car.display_info()