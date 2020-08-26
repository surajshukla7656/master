from math import pi

def cal_csa(radius, height):
    return 2 * pi * radius * height

def cal_tsa(radius, height):
    return 2 * pi * radius * height + 2 * pi * radius ** 2

def cal_vol(radius, height):
    return pi * ( radius ** 2 ) * height
from math import pi, sqrt

def cal_csa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return  pi * radius * l

def cal_tsa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return pi * radius * l + pi * radius ** 2

def cal_vol(radius, height):
    return  (1 / 3) * pi * ( radius ** 2 ) * height
import cylinder, cone

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cylinder.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cylinder.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cylinder.cal_vol(r, h))

print()

print("Enter the dimensions of the cone:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cone.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cone.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cone.cal_vol(r, h))
python main_prog7.py

def cal_csa(radius, height):
    return 2 * pi * radius * height

def cal_tsa(radius, height):
    return 2 * pi * radius * height + 2 * pi * radius ** 2

def cal_vol(radius, height):
    return pi * ( radius ** 2 ) * height
from math import pi, sqrt

def cal_csa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return  pi * radius * l

def cal_tsa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return pi * radius * l + pi * radius ** 2

def cal_vol(radius, height):
    return  (1 / 3) * pi * ( radius ** 2 ) * height
# module aliasing

import cylinder as cy, cone as cn

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cy.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cy.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cy.cal_vol(r, h))

print()

print("Enter the dimensions of the cone:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cn.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cn.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cn.cal_vol(r, h))
# member aliasing

from cylinder import cal_csa as csa, cal_tsa as tsa, cal_vol

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %csa(r, h))
print("Total surface area(in sq. units): %.2f" %tsa(r, h))
print("Volume(in cu. units): %.2f" %cal_vol(r, h))


ketan anand	
kunal sharma	
vikas 210	
suraj shukla	
vaibhav tiwari	
samrat chhabra	
himanshi sharma	
pawan joshi	
himanshu jha	
vishal kumar	
shivam kumar	
