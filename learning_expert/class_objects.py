
# functions used in defining a class

'''
__init__() 

'''

# Python Inheritance

'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

'''

# inheriting properties of parent class

'''
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

'''

# inheriting properties of parent class(using super())

'''
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

'''