#  Python program to create 
# a module 
    
# Defining a function 
def rpvv(): 
    print("C Sc students rock!") 
  
# Defining a variable 
location = "Raj Niwas Marg"
----------------------------------
# Python program to demonstrate 
# modules 
  
import module_1
  
# Use the function created 
module_1.rpvv() 
  
# Print the variable declared 
print(module_1.location) 

-------------------------------------
Run:
python main_prog1.py
OUTPUT:
C Sc students rock!
Raj Niwas Marg
#  Python program to create 
# a module 
    
# Defining a function 
def rpvv(): 
    print("C Sc students rock!") 
  
# Defining a variable 
location = "Raj Niwas Marg"
----------------------------------
# main_prog1.py :  Python program to demonstrate 
# modules 
  
import module_1 as m
  
# Use the function created 
m.rpvv() 
  
# Print the variable declared 
print(m.location) 

-------------------------------------
Run:
python main_prog1.py
OUTPUT:
C Sc students rock!
Raj Niwas Marg
import math

def circle_area(radius):
    return math.pi * radius ** 2

def square_area(side):
    return side ** 2

def rect_area(length, breadth):
    return length * breadth


def tri_area(a, b, c):
    s = (a + b + c) / 2
    return  math.sqrt(s * (s -a ) * (s - b) * (s -c))
-----------------------------
# main_prog2.py

import area

r = float(input("Enter radius of the circle: "))
print("Area of the circle (in sq. units) %.2f\n" %area.circle_area(r))

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
