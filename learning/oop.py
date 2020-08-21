# ------------------------- oop introduction --------------------->

# class Person:
#     def __init__(self,firstname,lastname,age)    :
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age

#     def categories(self):
#         if self.age>=60:
#             return f"{self.firstname} is old aged person"
#         elif self.age>18:
#             return f"{self.firstname} is an adult"
#         else:
#             return f"{self.firstname} is a teenager or child"

# p1=Person("suraj","shukla,",17)
# p2=Person("chandni","jaiswal",17)  
# print(p1.firstname)  
# print(p1.categories())
# print(Person.categories(p1))

# ------------------------ class varible ------------------------------>

#class variable

# class Circle:
#     pi=22/7
#     def __init__(self,radius):
#         self.radius=radius
        
#     def circumference(self):
#         return 2*Circle.pi*self.radius                  #Circle.pi ------> class varible ,here circle can be replaced by self if the variable changes with instance
#                                                         #class variable ---> <class_name>.<variable>
#                                                         #instance variabel ---> self.variable
# c1=Circle(3)
# print(c1.circumference())

# print(c1.__dict__)                                       #to show all data associated with an instance

# ------------------ class method -------------------->

# class Person:
#     count_instances=0
#     def __init__(self,firstname,lastname,age)    :
#         Person.count_instances =+ 1
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age

#     def categories(self):
#         if self.age>=60:
#             return f"{self.firstname} is old aged person"
#         elif self.age>18:
#             return f"{self.firstname} is an adult"
#         else:         
#             return f"{self.firstname} is a teenager or child"

#     @classmethod                                                                #generator for defining class methods
#     def count_instances(cls):                                                   #cls refers to class
#         return f"You have created {cls.count_instances} instances of {cls.__name__} class"

# p1=Person("suraj","shukla,",17)
# p2=Person("chandni","jaiswal",17)  
# print(p1.firstname)  
# print(p1.categories())
# print(Person.categories(p1))
# print(Person.count_instances())


# class Books:
#     def __init__(self,speciality,author,publication_year,price):
#         self.speciality=speciality
#         self.author=author 
#         self.year=publication_year
#         self.price=price

#     def discount(self,discount):
#         return (self.price)*(discount*.01)


# COP=Books("jee","hcverma",2993,1000)
# print(COP.__dict__)
# print(COP.discount(25))

# --------------------- class method as constructor ----------->

# class Person:
#     count_instances=0
#     def __init__(self,firstname,lastname,age)    :
#         Person.count_instances =+ 1
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age

#     def categories(self):
#         if self.age>=60:
#             return f"{self.firstname} is old aged person"
#         elif self.age>18:
#             return f"{self.firstname} is an adult"
#         else:         
#             return f"{self.firstname} is a teenager or child"

#     @classmethod                                                                #generator for defining class methods
#     # def count_instances(cls):                                                   #cls refers to class
#     #     return f"You have created {cls.count_instances} instances of {cls.__name__} class"

#     @classmethod
#     def fromstrings(cls,string):
#         firstname,lastname,age=string.split(",")
#         return cls(firstname,lastname,age)
# p1=Person("suraj","shukla,",17)
# p2=Person("chandni","jaiswal",17)  
# print(p1.firstname)  
# print(p1.categories())
# print(Person.categories(p1))
# # print(Person.count_instances())
# p3=Person.fromstrings("kuldeep,shukla,15")
# print(p3.__dict__)


#----------------------static method-------------->>

# using @staticmethod ----> neither link with class or instance but defined inside class




# ----------------------------theory------------------------>


#encapsulation------>writing data and methods associated with it together

#_<var>  
# 
#  ---> convention for private name

#__<var>__ ------> dunder/magic method

# __var -------> _cls__var (name mangling)

#--------------------decorator----------------->
# @property --------------> this is used to convert a func into instance variable

#@<var>.setter   ---------------> to set a instance variable, use just after the property

#@classmethod ----------------> to define a class method
#@staticmethod ------------------> to define a random method inside a class

# -----------------------------------inheritance --------------->
#base class/ parent class
#derived class/ child class


# class phone:
#     def __init__(self,brand,modelname,price):
#         self.brand=brand
#         self.modelname=modelname
#         self.price

#     def fullname(self):
#         return f"{self.brand}{self.modelname}"

# class smartphone(phone):
#     def __init__(self,brand,modelname,price,ram , internalmemory,rearcamera):
#         phone.__init__(self,brand,modelname,price)

#         super().__init__(brand,modelname,price)
#         self.ram=ram
#         self.internalmemory=internalmemory
#         self.rearcamera=rearcamera


#----------------->>>>>>>
#isinstance
#issubclass

# help(instance),c.mor(),c.__mor__

#dunder method

# def __repr__(self):
#     return <object>

# def __str__(self):
#     return <message while printing the class>

#def __len__(self):
#   pass

#def __add__(self,other):
#   return self.price+other.price


#polymorphism ---- more than one type