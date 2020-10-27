

# Function returning multiple values
def cal(m, n):
    sum = m + n
    diff = m - n
    return sum, diff

# Driver's code
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

s, d = cal(x, y)

print("The sum =", s )
print("The difference =", d)


# Python program to calculate curved surface area,
# total surface area and volume of
# a right circular cone using a function
# returning multiple values
# import specific components from math module
from math import sqrt
from math import pi

def cal(radius, height):
    l = sqrt( radius * 2 + height * 2) # slant height
    csa = pi * radius * l
    tsa = csa + pi * radius ** 2
    vol = (pi * (radius ** 2) * height)/ 3
    return csa, tsa, vol

# Driver's code
print("Enter the dimensions of the cone:")
r = float(input("\tRadius: "))
h = float(input("\tHeight: "))

# calling the function
curvedSurfaceArea, totalSurfaceArea, volume = cal(r, h)
print("Curved Surface Area (in sq. units) = %.2f" % curvedSurfaceArea)
print("Total Surface Area (in sq. units) = %.2f" % totalSurfaceArea)
print("Volume (in cu. units) = %.2f" % volume) 


#And how to implement your own module and use it in other Python programs:
 # Implementing calculate module
# calculate.py

# sum
def sum(m, n):
    return m + n

# difference
def diff(m, n):
    return m - n

# product
def prod(m, n):
    return m * n

# quotient
def quot(m, n):
    return m / n

# floor devision
def floor_div(m, n):
    return m // n

# remainder on division
def rem(m, n):
    return m % n


# Implementing a calculator
# using the concept of module

import calculate

# Driver's code
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

s = calculate.sum(x, y)
d = calculate.diff(x, y)
p = calculate.prod(x, y)
q = calculate.quot(x, y)
fd = calculate.floor_div(x, y)
r = calculate.rem(x, y)

print ("The sum = ", s)
print ("The difference = ", d)
print ("The product = ", p)
print ("The quotient = ", q)
print ("The floor division = ", fd)
print ("The remainder on division = ", r)


# Implementing a calculator
# using the concept of module

from calculate import *

# Driver's code
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

s = sum(x, y)
d = diff(x, y)
p = prod(x, y)
q = quot(x, y)
fd = floor_div(x, y)
r = rem(x, y)

print ("The sum = ", s)
print ("The difference = ", d)
print ("The product = ", p)
print ("The quotient = ", q)
print ("The floor division = ", fd)
print ("The remainder on division = ", r) 

# Implementing a calculator
# using the concept of module

from calculate import sum, diff, prod, quot, floor_div, rem

# Driver's code
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))

s = sum(x, y)
d = diff(x, y)
p = prod(x, y)
q = quot(x, y)
fd = floor_div(x, y)
r = rem(x, y)

print ("The sum = ", s)
print ("The difference = ", d)
print ("The product = ", p)
print ("The quotient = ", q)
print ("The floor division = ", fd)
print ("The remainder on division = ", r)


# Python program to calculate and
# display roots of a quadratic equation:
# a x**2 + b x + c = 0
# This program uses functions
# which return multiple values
#import math and complex math library
import math
import cmath

# Function to calculate real roots
def real_roots(a, b, c, D):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    return x1, x2

# Function to calculate imaginary roots
def img_roots(a, b, c, D):
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)
    return x1, x2

# Driver's code
# Prompt the user to enter the coefficients
print("Enter the coefficients of quadratic equation")
a = float(input("\ta: "))
b = float(input("\tb: "))
c = float(input("\tc: "))

# calculate discriminant
D = (b ** 2) - (4 * a * c)

if D >= 0:
    root1, root2 = real_roots(a, b, c, D)
    print("Roots are real numbers")
    print("first root = %.2f and second root = %.2f" %(root1, root2))
else:
    root1, root2 = img_roots(a, b, c, D)
    print("Roots are imaginary numbers")
    print("first root = {0} and second root = {1}".format(root1, root2))