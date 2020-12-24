import time 
import datetime
# # t1=time.time()
# # print(t1)
# # time.sleep(10)
# t2=time.time()

# print(time.ctime(t2))
# print(t2-t1)

t=time.time()
print(time.ctime())
result = time.localtime()
print(result)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# print(datetime.datetime.now())
time.sleep(10)
print(time.ctime(t))