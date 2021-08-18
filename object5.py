# 10/01/2021-----------
# Tamim Shahriar Subeen----
# Object Oriented Programming----------
# Class and Object-------------
# Inheritance------------


class Vehicle:
    """Base class for all vehicles"""  # Docstring----------

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping!")


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mastang 5.0 GT Coupe", "Ford", "Red")

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn("left")
    v2.turn("Right")

    v1.brake()
    v2.brake()
    v3.brake()


# Inheritance------------
class Vehicle:
    """Base class for all vehicles"""  # Docstring----------

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping!")


class car(Vehicle):
    """Car Class"""

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = car("Mustang 5.0 GT Coupe", "Ford", "Red")
    c.drive()
    c.brake()
    c.change_gear("P")


# Inheritance------------
class Vehicle:
    """Base class for all vehicles"""  # Docstring----------

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping!")


class car(Vehicle):
    """Car Class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4
        print("A new car has been created. Name:", self.name)
        print("It has", self.wheels, "wheels")
        print("The car was built in", self.year)

    def change_gear(self, gear_name):
        """Method of changing rear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = car("Mustang 5.0  GT Coupe", "Ford", "Red", 2017)


# Method Overriding----------------
class Vehicle:
    """Base class for all vehicles"""  # Docstring----------

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print("Turning", self.name, "to", direction)


class car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4


    def change_gear(self, gear_name):
        """Method of changing rear"""
        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):
        print(self.name, "is turning", direction)


if __name__ == "__main__":
    c = car("Mustang 5.0  GT Coupe", "Ford", "Red", 2017)
    v = Vehicle("Softail Delux", "Harley_Davidson", "Blue.")
    c.turn("right")
    v.turn("right")


# Method Overriding----------------
class Vehicle:
    """Base class for all vehicles"""  # Docstring----------

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        print("Creating a car")
        super().__init__(name, manufacturer, color)
        self.year = 2017
        self.wheels = 4


if __name__ == "__main__":
    c = car("Mustang 5.0  GT Coupe", "Ford", "Red", 2017)
    print(c.name, c.year, c.wheels)

# ----------End----------#
