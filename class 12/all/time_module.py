
# returns seconds from struct_time
s = time.mktime(t)
print("\ns:", seconds)
#  (or a tuple containing 9 elements corresponding to struct_time)
#  as an argument and returns a string representing it. Here's an example:
import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)
# (or tuple corresponding to it) as an argument 
# and returns a string representing it based on the format code used.
import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)
# a string representing time and returns struct_time.
import time

time_string = "21 June, 2020"
result = time.strptime(time_string, "%d %B, %Y")

print(result)
import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  time.sleep(1)
#  better version of the digital clock program.

import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)

import threading 
  
def print_hello_three_times():
  for i in range(3):
    print("Hello")
  
def print_hi_three_times(): 
    for i in range(3): 
      print("Hi") 

t1 = threading.Thread(target=print_hello_three_times)  
t2 = threading.Thread(target=print_hi_three_times)  

t1.start()
t2.start()
import threading 
import time
  
def print_hello():
  for i in range(4):
    time.sleep(0.5)
    print("Hello")
  
def print_hi(): 
    for i in range(4): 
      time.sleep(0.7)
      print("Hi") 

t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  
t1.start()
t2.start()
# Time intervals are floating-point numbers in units of seconds.
#  Particular instants in time are expressed in seconds
#  since 12:00am, January 1, 1970(epoch).
import time  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
import calendar

cal = calendar.month(2003, 5)
print ("Here is the calendar:")
print (cal)
import time
seconds = time.time()
print("Seconds since epoch =", seconds)
import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

local_time = time.ctime()
print("Local time:", local_time)
# execution of the current thread 
# for the given number of seconds.
import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
# the number of seconds passed since
#  epoch as an argument and returns struct_time in local time.
import time

result = time.localtime(1594788221)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
#  passed since epoch as an argument 
# and returns struct_time in UTC.
import time

result = time.gmtime(1594876197)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_min:", result.tm_min)

result = time.localtime(1594876197)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_min:", result.tm_min)
import datetime

date_object = datetime.date.today()
print(date_object)

import datetime

d = datetime.date(2019, 4, 13)
print(d)
from datetime import date

today = date.today()

print("Current date =", today)
# We can also create date objects 
# from a timestamp. 
# A Unix timestamp is the number of seconds
#  between a particular date and January 1, 1970 at UTC.
#  You can convert a timestamp to date 
# using fromtimestamp() method.
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
# A time object instantiated 
# from the time class represents the local time.

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

from datetime import datetime

# datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))
roll no. 12515

Hello everyone.....here's the video on CBSE DELETED TOPICS Class XII ENGLISH CORE - and RATIONALISED CURRICULUM 2020-21.....
Kindly add the following no to this grp

Bio Pdf
📷https://drive.google.com/drive/folders/1JDD1ARp5uoGorRO4qFQoqM6W99Lr4YSx?usp=sharing
Chemistry pdf
📷https://drive.google.com/drive/folders/1T1kymbqE4BD5mHiMkZMb3e-cy8qqRwFs?usp=sharing
maths pdf
📷https://drive.google.com/drive/folders/1zBnVb9V0L1dg-TiM03fOWzEOFKA2ayOt?usp=sharing
physics pdf
📷https://drive.google.com/drive/folders/1B5iTE0jGnxZRcEocpZSr3b2aQyxYu3a8?usp=sharing
