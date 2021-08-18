# 10/01/2021-----------
# Tamim Shahriar Subeen----
# Object Oriented Programming----------
# Class and Object-------------


class car:
    name = "Primio"
    color = "White"

    def start():
        print("Starting the engine")


print("Name of the car:", car.name)
print("Color: ", car.color)
car.start()


# Class and Object-------------
class car:
    name = ""
    color = ""

    def start():
        print("Starting the engine")


car.name = "Axio"
car.color = "Black"
print("Name of the car:", car.name)
print("Color: ", car.color)
car.start()
print(dir(car))


# Class and Object-------------
class car:
    name = ""
    color = ""

    def start(self):
        print("starting the engine")


my_car = car()
my_car.name = "Allion"
print(my_car.name)
my_car.color = "black"
print(my_car.color)
my_car.start()


# Class and Object-------------
class car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("starting the engine")


my_car = car("Corolla", "White")
print(my_car.name)
print(my_car.color)
my_car.start()


# Class and Object-------------
class car:
    def __init__(self, n, c, y):
        self.name = n
        self.color = c
        self.year = y

    def start(self):
        print("name: ", self.name)
        print("color: ", self.color)
        print("Year: ", self.year)
        print("Starting the engine")


# Object---
my_car = car("Corolla", "White", 2019)
my_car.start()
my_car1 = car("BMW", "black", 2020)
my_car1.start()
my_car2 = car("Alion", "black", 2021)
my_car2.start()

# ----------END---------- #
