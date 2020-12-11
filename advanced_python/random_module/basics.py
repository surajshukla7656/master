'''
Method	                          Checklist                                 Description
seed(seed value=current system time) ##                                     Initialize the random number generator
getstate()	                         ##                                     Returns the current internal state of the random number generator
setstate(random.getstate())	         ##                                     Restores the internal state of the random number generator
getrandbits(n)	                     ##                                     Returns a number representing the random bits
randrange(start,stop,step)	         ##                                     Returns a random number between the given range
randint(start,stop)	                 ##                                     Returns a random number between the given range,includes extremities
choice()	                         ##                                     Returns a random element from the given sequence
choices(seq,weights/cum_weights,k)   ##                                     Returns a list with a random selection from the given sequence
shuffle(seq,function)                ##                                     Takes a sequence and returns the sequence in a random order
sample(seq,k)	                     ##                                     Returns a given sample of a sequence
random()	                         ##                                     Returns a random float number between 0 and 1
uniform(low, hight)             	 ##                                     Returns a random float number between two given parameters
triangular(low,high,mode)	         ##                                     Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	                                                            Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	                                                            Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()	                                                            Returns a random float number based on the Gamma distribution (used in statistics)
gauss()	                                                                    Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()	                                                        Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()	                                                            Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()	                                                        Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()	                                                            Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()	                                                        Returns a random float number based on the Weibull distribution (used in statistics)

'''

import random


# ##### seed ##### 

# # seed value - a number from which random number generator starts

# # random.seed(4.4)                                      # return None --- using same seed value generates same random number --- by default uses system time as a seed value

# ##### getstate #####

# a=random.getstate()                                     # return current internal  state of random number generator

# ##### setstate #####

# random.setstate(a)                                     # retores interanl state of random number generator --- return None

# # print(a)
# print(random.random())

# ##### getrandbits ######

# # n - any integer greater than 0

# a=random.getrandbits(1)                                 # returns random decimal number which have <=n bits in binay form


# ##### randrange #####

# a=random.randrange(4)                                   # return random number between specified range --- not includes extremities

# print(a)

 
# ##### randint ##### 

# a=random.randint(3,4)                                   #  return random int number between specified range --- includes extremities

# print(a)

# ##### choice #####

# l=('apple','banana','mango')

# a=random.choice(l)                                        # returns a random element from an iterator

# print(a)

# ##### choices #####

# # seq - a iterator

# # weights - require iterable with length = to number element in l(iterator)

# # cum_weights - require iterable with length = to number element in l(iterator) --- this time possibility is accumulated(unable to uderstand)

# # k = length of returned list ( by default - 1)

# l=('apple','banana','mango')

# a=random.choices(l,weights=(2,1,1),k=6)                       

# print(a)

# a=random.choices(l,cum_weights=[2,5,3],k=6)


# print(a)

# ##### shuffle #####

# function - a function that returns number between 0 and 1 --- by default uses random function

# l=['apple','banana','mango']

# random.shuffle(l)                    # return None --- shuffles the existing list

# print(l)

# ##### sample #####

# # seq - an iterator 

# # k = length of returned string --- should be <= seq length

# l=('apple','banana','mango')

# a=random.sample(l,k=3)                 # returns a list with randomly selected elements of specified length

# print(a)

##### random #####

# print(random.random())                   # returns random number between 0  and 1 

##### uniform #####

# low - lowest value

# high - highest value 

# print(random.uniform(30,50))              # returns floating number between given range --- includes extremities

##### triangular #####

# low - lowest value

# high - highest value 

# mode - tending to --- by default midpoint of low and high