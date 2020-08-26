import math

def circle_area(radius):
    return math.pi * radius ** 2

def square_area(side):
    return side ** 2

def rect_area(length, breadth):
    return length * breadth

def tri_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s -a) * (s - b) * (s -c))
# import area module
import area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f\n" %area.circle_area(r))

side = float(input("Enter the side of the square: "))
print("Area of the square (in sq. units) %.2f\n" %area.square_area(side))

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle (in sq. units) %.2f\n" %area.rect_area(length, breadth))

print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %area.tri_area(a, b, c))
# import area module
from area import *

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f\n" %circle_area(r))

side = float(input("Enter the side of the square: "))
print("Area of the square (in sq. units) %.2f\n" %square_area(side))

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle (in sq. units) %.2f\n" %rect_area(length, breadth))

print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %tri_area(a, b, c))
# import area module
from area import circle_area, tri_area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f\n" %circle_area(r))



print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %tri_area(a, b, c))

import math

#### LIBRARY TO FIND AREA OF * CIRCLE , * CYLINDER , * CONE ####

##AREA OF CIRCLE 

def circle(radius) :
    area=math.pi*(radius**2)
    return area

##AREA OF CONE 
        
def cone(radius,height) :
    area=1/3*(math.pi*(height*(radius**2)))
    return area

##AREA OF CYLINDER    
            
def cylinder(radius,height) :
    area=math.pi*(height*(radius**2))
    return area

#### SINGLE AREA ACCESSING MODULE ####
                
def area_show(argument) :
    argument2=argument.lower()
    if argument2.strip()=="circle" :
        rads=int(input("Enter Radius of Circle : "))
        print("%.4f"%circle(rads))
       
    elif argument2.strip()=="cone" :
        rads=int(input("Enter Radius of Cone : "))
        heis=int(input("Enter Height of Cone :"))
        print("%.4f"%circle(rads,heis))
       
    elif argument2.strip()=="cylinder" :
        rads=int(input("Enter Radius of Cylinder : "))
        heis=int(input("Enter Height of Cylinder :"))     
        print("%.4f"%cylinder(rads,heis))
        
    else :
        print(f"ERROR OCCURED : THIS MODULE {argument} IS NOT IN <Xarea> MODULE .")
import Xarea

Xarea.area_show("circle")
print()

Xarea.area_show("cone")
print()

Xarea.area_show("cylinder")
print()


from math import pi

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2
# import module circle
import circle

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %circle.area(r))
print("Circumference of the circle = %.2f" %circle.circumference(r))
# import module circle
from circle import *

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %area(r))
print("Circumference of the circle = %.2f" %circumference(r))
# import module circle
from circle import area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %area(r))
