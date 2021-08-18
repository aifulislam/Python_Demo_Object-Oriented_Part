# 10/01/2021-----------
# Tamim Shahriar Subeen----
# Object Oriented Programming----------
# Class and Object-------------
# Inheritance------------
# Turtle-------------

import turtle


class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        print("I won't turn right, because I am ajob!")


if __name__ == "__name__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

    jonto = turtle.Turtle()
    jonto.shape("turtle")
    jonto.left(30)
    jonto.forward(200)
    jonto.left(45)
    jonto.backward(100)
    jonto.right(90)
    jonto.forward(10)

turtle.done()

# ----------End------------#
