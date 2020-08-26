 os package 
 sys package
from math import pi, sqrt

def cylinder_csa(radius, height):
    return 2 * pi * radius * height

def cone_csa(radius, height):
    l = sqrt(height ** 2 + radius ** 2)
    return pi * radius * l
from math import pi, sqrt

def cylinder_tsa(radius, height):
    return 2 * pi * radius * height + 2 * pi * radius ** 2

def cone_tsa(radius, height):
    l = sqrt(height ** 2 + radius ** 2)
    return pi * radius * l + pi * radius ** 2
from math import pi

def cylinder_vol(radius, height):
    return pi * (radius ** 2) * height

def cone_vol(radius, height):
    return (1 / 3) * pi * (radius ** 2) * height
# import package
from mensuration import csa, tsa, vol

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %csa.cylinder_csa(r, h))
print("Total surface area(in sq. units): %.2f" %tsa.cylinder_tsa(r, h))
print("Volume(in cu. units): %.2f" %vol.cylinder_vol(r, h))

print()

print("Enter the dimensions of the cone:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %csa.cone_csa(r, h))
print("Total surface area(in sq. units): %.2f" %tsa.cone_tsa(r, h))
print("Volume(in cu. units): %.2f" %vol.cone_vol(r, h))
Rollno 12529
Roll no 12520
I am unable to join

We are proud to announce EMC's 6th Digital *Live Entrepreneur Interaction (Digital LEI)*.

 *Ms Sujata and Ms Taniya*, *(Founders- Suta)* will be interacting live with our students and teachers through the SCERT Delhi youtube channel.

*Chief Guest : Shri Manish Sisodia (Deputy Chief Minister, Delhi)* 

*Guest of Honour* : Mrs Manisha Saxena | IAS, Secretary (Education) , Delhi
Date : 15th July (Wednesday), 2020
Time : 12:00 pm
YouTube channel:
https://bit.ly/SCERTDelhiYT
