"""
Luke Russell
Area Calculator 2
4/1/21
"""
import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ""

while shape != "quit":
    shape = input("What shape would you like to calculate area for? ")
    shape = shape.lower()
    if shape == "square":
        side = float(input("What is the length of the side of the square? "))
        areaS = compute_area_square(side)
        
    elif shape == "rectangle":
        length = float(input("What is the length of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        areaR = compute_area_rectangle(length,width)

    elif shape == "circle":
        radius = float(input("What is the radius of the circle? "))
        areaC = compute_area_circle(radius)

print(f"The area of the square is {areaS}.")
print(f"The area of the rectangle is {areaR}.")
print(f"The area of the circle is {areaC}.")