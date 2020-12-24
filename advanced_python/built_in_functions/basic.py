#Python Built in Functions

'''
Function              checklist         	Description

abs()	                 ##                 Returns the absolute value of a number
all()	                 ##                 Returns True if all items in an iterable object are true
any()	                 ##                 Returns True if any item in an iterable object is true
ascii()	                                    Returns a readable version of an object. Replaces none-ascii characters with escape character
bin(n)	                 ##                 Returns the binary version of a number
bool()	                 ##                 Returns the boolean value of the specified object
bytearray(x,encoding,e)  #                  Returns an array of bytes --- can be modified
bytes(x,encoding,error)	 #                  Returns a bytes object --- cannot be modified 
callable(obj)  	         ##                 Returns True if the specified object is callable, otherwise False
chr(int)	             ##                 Returns a character from the specified Unicode code.
classmethod()	                            Converts a method into a class method
compile(s,f,m,f,d,o)     ##                 Returns the specified source as an object, ready to be executed
complex(real,imaginary)	 ##                 Returns a complex number
delattr(obj,attribute)   ##                 Deletes the specified attribute (property or method) from the specified object
dict()	                 ##                 Returns a dictionary (Array)
dir(obj)                 ##                 Returns a list of the specified object's properties and methods
divmod(ar1,arg2)         ##                 Returns the tuple of quotient and the remainder when argument1 is divided by argument2
enumerate(iterable,start)##                 Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval(express,g,l)	     ##                 Evaluates and executes an expression
exec(blocks,g,l)	     ##                 Executes the specified code (or object)
filter()	             ##                 Use a filter function to exclude items in an iterable object
float()        	         ##                 Returns a floating point number
format(value,format)                        Formats a specified value
frozenset(iterable)                         Returns a frozenset object
getattr(obj,attribute,message)	            Returns the value of the specified attribute (property or method)
globals()	                                Returns the current global symbol table as a dictionary
hasattr(obj,attribute)   ##                 Returns True if the specified object has the specified attribute (property/method)
hash()	                                    Returns the hash value of a specified object
help()	                 ##                 Executes the built-in help system
hex(integer)	         ##                 Converts a number into a hexadecimal value
id(obj)	                 ##                 Returns the id of an object
input(prompt)            ##                 Allowing user input
int(value,base)          ##                 Returns an integer number
isinstance(obj,class)	 ##                 Returns True if a specified object is an instance of a specified object
issubclass(child,parent) ##                 Returns True if a specified class is a subclass of a specified object
iter()         	                            Returns an iterator object
len()	                 ##                 Returns the length of an object
list(iterable)           ##                 Returns a list
locals()	                                Returns an updated dictionary of the current local symbol table
map(func,iterabl)        ##                 Returns the specified iterator with the specified function applied to each item
max(iterable)            ##                 Returns the largest item in an iterable
memoryview()	                            Returns a memory view object
min(iterable)            ##                 Returns the smallest item in an iterable
next(iterator,ending)    ##                 Returns the next item in an iterable
object()	                                Returns a new object
oct(int)	             ##                 Converts a number into an octal
open(file,mode)          ##                 Opens a file and returns a file object
ord(char)                                   Convert an integer representing the Unicode of the specified character(string of lenght 1)
pow(x,y,modulus)         ##                 Returns the value of x to the power of y --- (x**y)%z
print(o,s,e,f,f,)        ##                 Prints to the standard output device
property()	                                Gets, sets, deletes a property
range(start,stop,step)   ##                 Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	                                    Returns a readable version of an object
reversed(iterable)                          Returns a reversed iterator
round(number,decimalexpa)##	                Rounds a numbers --- default 0
set()	                                    Returns a new set object
setattr(o,a,v)	         ##                 Sets an attribute (property/method) of an object
slice(start,stop,step)   ##                 Returns a slice object
sorted(i,k,r)            ##                 Returns a sorted list
@staticmethod()	                            Converts a method into a static method
str(o,e,e)               ##                 Returns a string object
sum(iterable,step)       ##                 Sums the items of an iterator
super()	                 ##                 Returns an object that represents the parent class
tuple()     	         ##                 Returns a tuple
type()	                 ##                 Returns the type of an object
vars()	                                    Returns the __dict__ property of an object
zip(i1,i2,i3,...)        ##                 Returns an iterator, from two or more iterators

'''

# ##### abs ##### 

# print(abs(-4))

# ##### all #####
# l= ['suraj','f']

# print(all(l))                   # return True

# l= ['suraj', ' ']

# print(all(l))                   # return True 

# l=['surajs','']

# print(all(l))                   # return False

# ##### any #####

# l= ['suraj','f']

# print(any(l))                   # return False

# l= ['suraj', ' ']

# print(any(l))                   # return False

# l=[0,'']

# print(any(l))                   # return True

##### bin #####

# print(bin(3))                     # return binary value of int

# ##### bool ##### 

# print(bool(4))

# bool() # it returns false only for empty values 

# # bool return false in these input
# print(f'''
# {bool(False)}
# {bool(None)}
# {bool(0)}
# {bool("")}
# {bool(())}
# {bool([])}
# {bool({})}''')

##### callable #####


# def func():
#     True

# x=3
# print(callable(func))          # returns True

# print(callable(x))             # return False


##### chr #####

# print('a to z\n')

# for i in range(97,123):                 # return a to b

#     print(i,'-',chr(i))                 

# print('\nA to Z\n')

# for i in range(65,91):                  # return A to B

#     print(i,'-',chr(i))                 

# print('\n0 to 9\n')
# for i in range(10):                     # return 0 to 9

#     print(i,'-',chr(i))  

# print()          

##### compile #####

# compile(source, filename, mode, flag, dont_inherit, optimize)

# source	       -Required. The source to compile, can be a String, a Bytes object, or an AST object
# filename	       -Required. The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like
# mode	           -Required. Legal values:
                        # eval             - if the source is a single expression
                        # exec             - if the source is a block of statements
                        # single           - if the source is a single interactive statement
# flags	           -Optional. How to compile the source. Default 0
# dont-inherit	   -Optional. How to compile the source. Default False
# optimize	       -Optional. Defines the optimization level of the compiler. Default -1


# x = compile('print(55)', 'test', 'eval')
# exec(x)

# x = compile('print(55)\nprint(88)', 'test', 'exec')
# exec(x)

##### complex #####

# x=complex(3,4)             # return 3+4j
# print(x)

# x=complex(3+4j)
# print(x)

##### dict #####

# x=dict(name = 'surajshukla',_class=12)

# print(x)

##### divmod #####

# print(divmod(4,5))

##### enumerate #####
# x=dict(name = 'surajshukla',_class=12)

# print(enumerate(x))                         # converting into enumerate object

# for i in enumerate(x,3):

#     print(i)

##### eval #####
#expression	 - A String, that will be evaluated as Python code
#globals	 - Optional. A dictionary containing global parameters
#locals	     - Optional. A dictionary containing local parameters

##### exec #####

# block      - A String, or a code object
# globals    - Optional. A dictionary containing global parameters
# locals	 - Optional. A dictionary containing local parameters

# x = 'name = "John"\nprint(name)'
# exec(x)

##### filter #####

# ages = [5, 12, 17, 18, 24, 32]

#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)

# for x in adults:kk
#   print(x)


# function	-A Function to be run for each item in the iterable
# iterable	-The iterable to be filtered


##### format #####

# x=format(34,'>')

# print(x)

##### getatter #####

# object	-Required. An object.
# attribute	-The name of the attribute you want to get the value from
# default	-Optional. The value to return if the attribute does not exist

# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"

# x = getattr(Person, 'age')

# class Person:
#   name = "John"
#   age = 36
#   country = "Norway"

# x = getattr(Person, 'age')                                          # return  True

# x = getattr(Person, 'page', 'my message')                           # return False

##### globals #####


# print(globals())                                                   # returns important features of the current program

# print(globals()['__file__'])


##### help #####

# print(help())

##### id #####

# constant id for int -5 to 256

# x=-9

# print(id(x))

# b=id(x)


# print(id(b))

##### int #####

#base --- number system --- by default 10

# print(int('13',8))

##### iter #####

# object	-Required. An iterable object
# sentinel	-Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel

##### locals #####
# print(locals())

# print(globals())

##### ord #####

# print(ord('2'))

# ##### pow #####

# pow(3,4,3)                     # (3 raised to the power 4)%3

##### print #####

# print(object(s), sep=separator, end=end, file=file, flush=flush)


# object(s)	         - Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	 - Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	         - Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	             - Optional. An object with a write method. Default is sys.stdout
# flush	             - Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False


##### setattr #####

# object	       - Required. An object.
# attribute	       - Required. The name of the attribute you want to set
# value	           - Required. The value you want to give the specified attribute


##### slice #####

# start	  - Optional. An integer number specifying at which position to start the slicing. Default is 0
# end	  - An integer number specifying at which position to end the slicing
# step	  - Optional. An integer number specifying the step of the slicing. Default is 1


# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(0, 8, 3)
# print(a[x])


##### #####

# sorted(iterable, key=key, reverse=reverse)

# iterable	     - Required. The sequence to sort, list, dictionary, tuple etc.
# key	         - Optional. A Function to execute to decide the order. Default is None
# reverse	     - Optional. A Boolean. False will sort ascending, True will sort descending. Default is False


##### str #####

# object	- Any object. Specifies the object to convert into a string
# encoding	- The encoding of the object. Default is UTF-8
# errors	- Specifies what to do if the decoding fails


##### super #####

# class Parent:
#   def __init__(self, txt):
#     self.message = txt

#   def printmessage(self):
#     print(self.message)

# class Child(Parent):
#   def __init__(self, txt):
#     super().__init__(txt)

# x = Child("Hello, and welcome!")

# x.printmessage()


##### type #####

# object	- Required. If only one parameter is specified, the type() function returns the type of this object
# bases	    - Optional. Specifies the base classes
# dict	    - Optional. Specifies the namespace with the definition for the class
