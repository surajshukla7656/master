---------------------------front end----------------------------
member no:5
member name :surajshukla
age:18


---------------------------rear end----------------------------


---------------------------front end----------------------------
member no:5
member name :surajshukla
age:18


member no:4
member name :suraj
age:4


---------------------------rear end----------------------------

def enqueue(queue : list , item):
    queue.append(item) #concating the item

def dequeue(queue: list):
    return queue.pop(0) #popping and returning the element at index 0 

def display(queue : list):
    print(queue)


class Queue():
    __slots__ = ['data']
    def __init__(self , *args):
        if args:
            self.data = list(args)
        else:
            self.data = []

    def enqueue(self,item):
        self.data.append(item)
    
    def dequeue(self):
        return self.data.pop(0)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for i in self.data:
            yield i
    def toList(self):
        return self.data

class Queue3(collections.UserList):
    # another method to implement queueu
    def __init__(self, *args):
        if args:
            self.data = list(args)
        else:
            self.data = []


    def enqueue(self,item):
        self.data += item

    def dequeue(self):
        return self.data.pop(0) 

if __name__ =='__main__':
    ourqueue = [1,2,3]
    print('Our queue is ',ourqueue)
    enqueue(ourqueue,24)
    print('after appending 24')
    display(ourqueue)
    print(dequeue(ourqueue))



    l = Queue(1,2,3)
    print('The lenght of our queue',len(l))
    print('Queue is',l)
    for i in l:
        print(i) #iterating over the queue

    l.enqueue(123) # appending in the queue
    print('The queue after enqueue :',l) 
    print('The type of queue',type(l))
    print('After converting our queue in list',l.toList())
    print(l.dequeue())
    print(l)
    m = Queue3(1,2,3)
    print(len(m))
    print(m)
Our queue is  [1, 2, 3]
after appending 24
[1, 2, 3, 24]
The lenght of our queue 3
Queue is [1, 2, 3]
The queue after enqueue : [1, 2, 3, 123]
The type of queue <class '__main__.Queue'>
After converting our queue in list [1, 2, 3, 123]
[2, 3, 123]
[1, 2, 3]
#
# enqueue(queue, item), dequeue(queue) and display(queue)
# The item contains the following fields:
# member_no    :    integer
# member_name    :    string
# age	:	integer


# Checks If Queue Is Empty
def isQueueEmpty(queue) :
	
	if len(queue) == 0 :
	    return True
	    
	else :
	    return False


# Enqueue The Item At Last Of Queue
def enqueue(queue, item) :
    
    if (not (isinstance(item , (list , tuple , dict)))) :
        
        print("Only List And Tuple Are Allowed As Item To Be Enqueue")
        print()
    
    
    
    elif (len(item) != 3) :
        
        print("Only Member_no , Member_name , Age Are Allowed As Fields Of Item")
        print()
    
    
    
    elif (not (isinstance(item[0] , int) and isinstance(item[1] , str) and isinstance(item[2] , int))) :
        
        print("""Fields In Item Should Be As Per :
        
        member_no    :    integer
        member_name    :    string
        age	:	integer

        """)
      
       
    else :
        
        item = tuple(item)
        queue.append(item)
    

# Dequeue The Item From Starting Of Queue
def dequeue(queue) :
    
    if isQueueEmpty(queue) :
        
        print("Queue is empty")
        
    else :
        
        print(f"{queue.pop(0)} is dequeued from the Queue")
        

# Display The Queue
def display(queue) :
    
    print("_" * 45)
    print("member_no\tmember_name\t\tage")
    print("_" * 45)
    
    for member in queue :
        
        for i in range(len(member)) :
            
            print(member[i] , end = "\t\t")
            
        print()
    
    print("_" * 45)    
    print()
        
        
if __name__ == "__main__" :
    
    Q = []
    
    display(Q)
    dequeue(Q)
    
    enqueue(Q , (12501 , "Kunal Sharma" , 17))
    enqueue(Q , [12516 , "Aman Sharma" , 17])
    enqueue(Q , (12508 , "Vikas Kumar" , 17))
    enqueue(Q , (12519 , "Vaibhav Tiwari" , 17))
    enqueue(Q , [12521 , "Ketan Anand" , 17])
    enqueue(Q , (12522 , "Himanshu Jha" , 17))
    # etc .......
    
    
    display(Q)
    
    dequeue(Q)
    dequeue(Q)
    
    display(Q)
    
    dequeue(Q)
    dequeue(Q)
    dequeue(Q)
    dequeue(Q)
    
    
    display(Q)
    
    dequeue(Q)
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

Queue is empty
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

(12501, 'Kunal Sharma', 17) is dequeued from the Queue
(12516, 'Aman Sharma', 17) is dequeued from the Queue
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

(12508, 'Vikas Kumar', 17) is dequeued from the Queue
(12519, 'Vaibhav Tiwari', 17) is dequeued from the Queue
(12521, 'Ketan Anand', 17) is dequeued from the Queue
(12522, 'Himanshu Jha', 17) is dequeued from the Queue
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

Queue is empty
def IsQueueEmpty(queue):
    if len(queue) == 0:
       return True
    else:
     return False


# Puting an element at the rear end 
def Enqueue(queue, member_no, member_namestring, age):
    queue.append(member_no)
    queue.append(member_namestring)
    queue.append(age)

# deleting an element from the front end

def Dequeue(queue):
  if IsQueueEmpty (queue):
        print("Queue is Empty")

  else: 
   item = queue.pop(0)
   print(f" The elements deleted from the queue:{item}")
   print()  
#Displaying queue
def Display(queue):
     if IsQueueEmpty(queue):
          print("Queue is empty")

     else: 
         front = 0 
         rear = len(queue) -1
         for i in range(front, rear +1):
             print(queue[i],end = ' ')
          
#Executable code
if __name__ ==  "__main__":
 
    q = []
    Display(q)

    Enqueue(q,121, "abc", 17 )
    Enqueue(q,202, "adc",18)
    Enqueue(q,103, "ghg",19)
    Enqueue(q,204, "ghj",20)

    Display(q)

    Dequeue(q)
    Dequeue(q)

    Display(q)

    Dequeue(q)
    Dequeue(q)
def IsQueueEmpty(queue):
    if len(queue) == 0:
       return True
    else:
     return False


# Puting an element at the rear end 
def Enqueue(queue, member_no, member_namestring, age):
    queue.append(member_no)
    queue.append(member_namestring)
    queue.append(age)

# deleting an element from the front end

def Dequeue(queue):
  if IsQueueEmpty (queue):
        print("Queue is Empty")

  else: 
   item = queue.pop(0)
   item = queue.pop(0)
   item = queue.pop(0)
   print(f" The elements deleted from the queue:{item}")
   print()  
#Displaying queue
def Display(queue):
     if IsQueueEmpty(queue):
          print("Queue is empty")

     else: 
         front = 0 
         rear = len(queue) -1
         for i in range(front, rear +1):
             print(queue[i],end = ' ')
          
#Executable code
if __name__ ==  "__main__":
 
    q = []
    Display(q)

    Enqueue(q,121, "abc", 17 )
    Enqueue(q,202, "adc",18)
    Enqueue(q,103, "ghg",19)
    Enqueue(q,204, "ghj",20)

    Display(q)

    Dequeue(q)
    Dequeue(q)

    Display(q)

    Dequeue(q)
    Dequeue(q)
DISPLAY(stack)
The emp_data contains the following fields:
emp_no 	integer
emp_name	string
emp_post	string
emp_salary	float
# using list

# Check whether the Queue is empty
def isqueueEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

# Adding elements to the queue   
def enqueue(queue,member_no,member_namestring,age):
    queue.append(member_no)
    queue.append(member_namestring)
    queue.append(age)

# removing item from the queue
def dequeue(queue):
    if isqueueEmpty(queue):
        print("queue is empty")
    else:
        item = queue.pop(0)
        print("The element popped: " + str(item))

# Display the contents of the queue
def display(queue):
    if isqueueEmpty(queue):
        print("queue is empty")
    else:
        front = 0
        rear = len(queue)-1
        for i in range(front,rear + 1):
            print(queue[i],end=' ')
            print()
        


# Executable code
if name == "main" :
    a =[]
    display(a)

    enqueue(a,12501,"Kunal sharma",17)
    enqueue(a,12516,"Aman sharma",17)
    enqueue(a,12519,"Vaibhav sharma",17)
    enqueue(a,12521,"Ketan Anand",17)
    enqueue(a,12522,"Himanshu Jha",17)
    display(a)
    
    dequeue(a)
    dequeue(a)
    dequeue(a)
    

    display(a)
    

    dequeue(a)
    dequeue(a)
    dequeue(a)

    display(a)
## code after execution::                                                                                                                       queue is empty
Kunal sharma 
Aman sharma 
Vaibhav sharma 
Ketan Anand 
Himanshu Jha 
The element popped: 12501
The element popped: Kunal sharma
The element popped: 17
Aman sharma 
Vaibhav sharma 
Ketan Anand 
Himanshu Jha 
The element popped: 12516
The element popped: Aman sharma
The element popped: 17
Vaibhav sharma 
Ketan Anand 
Himanshu Jha 
C (graphite)    + 1/2 O2    ⇌   CO
at 25° C and 1 atm, ΔH  = -110525 J. What is ΔE, if the molar volume of graphite is 0.0053 L?

class PyQueue :
    
    def __init__(self,fields) :
        if type(fields)==list :
            self.queue=[]
            self.queuefields=[]
            if len(fields)!=0 :                
                for field in fields :
                    self.queuefields.append(field)
            else :
                self.queuefields=["Test1"]
        else :
            raise NameError(f"{fields} :  __Invalid Fields type__ Entered in PyQueue Implementation .")
    
    def isPyQueue(collection) :
        result=None
        if type(collection)==PyQueue :
            result=True
        else :
            result=False
        
        return result
    
    def QueueSize(self) :
        return len(self.queue)
        
    
    def isQueueEmpty(self) :
        result=None 
        if self.QueueSize()==0 :
            result=True
        else :
            result=False
            
        return result
    
    def QueueFields(self) :
        return self.queuefields
        
    def Enqueue(self,item) :
        if type(item)==list :
            if len(self.queuefields)==len(item) :
                entry={}
                for i in range(1,len(self.queuefields)+1) :
                    entry[self.queuefields[i-1]]=item[i-1]
                self.queue.insert(0,entry)
            else :
                raise InputError(f":: 2 :: {item} Items are {len(items)} More than {self.Queue} Items {self.QueueSize()}")
        else :
            raise InputError(f":: 1 :: {item} type {type(item)} : Invalid Input .")
            
    def Dequeue(self) :
        if self.isQueueEmpty()==False :
            self.queue.pop(0)
        else :
            print(f"EmptyQueueError : {self.queue} Empty Queue .")
    
    def QueueCopy(self) :
        result=self.queue[:]
        return Queue(result)
        
    def QueueDisplayVertical(self) :
        print()
        print("•|•|"*8)
        print()
        
        print(f"\t\t  ____CONSUMER 🚀 END____ ")
        print()
        print("_"*60)
        print()
        for i in self.queuefields :
            print(i,end="\t         ")
        print()
        print()
        
        for k in range(self.QueueSize()) :
            print("-"*60)
            print(f"\t\t\t--QUEUE ENTRY {k+1}--")
            for j in self.queue[k].values() :
                print(f" __{j}__ ",end=" -- ")
            print("-"*56)
        print()
        print("_"*60)
        print()
        print(f"\t\t  ____PRODUCER 🎉 END____ ")
        print()
        print("•|•|"*8)
        print()
  
-_----__--__Output__--____---



•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|

                  ____CONSUMER 🚀 END____

____________________________________________________________
Company          PODUCT          Price           Rating     

------------------------------------------------------------                        --QUEUE ENTRY 1--
 __Applex__  --  __Ixphone__  --  __x1opn90__  --  __5.0__  -- --------------------------------------------------------

____________________________________________________________
                  ____PRODUCER 🎉 END____

•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|

from queuePython import PyQueue

queue1=PyQueue(fields=["Company","PODUCT","Price","Rating"])

print(queue1)

queue1.Enqueue(item=["Applex","Ixphone","x1opn90","5.0"])

queue1.QueueDisplayVertical()

print(queue1.isQueueEmpty())
(1) Insert a record in the queue
(2) Delete a record from the queue
(3) Display the waiting list
Implement record as a list containing following fields.
Waiting_no   			Integer
(b)   R (2 π – 1) θ  / (4 π2)
(c)  R (2π – θ) / (4 π)
(d) R θ  / (2 π)
(2.0 atm, 3.0 L, 95 K) →(4.0 atm, 5.0 L, 245 K) with a change in internal energy, ΔU=30.0 Latm. The change in enthalpy ΔH of the process in L atm is:
a) 40.0



b) 42.3
c) 44.0
d) Not defined because pressure is not constant
(b)   R (2 π – 1) θ  / (4 π2)
(c)  R (2π – θ) / (4 π)
(d) R θ  / (2 π)

# module2.py

# A Module For

#A menu driven program in Python that allows the following operations on a 
# Queue of waiting list:
# (1) Insert a record in the queue
# (2) Delete a record from the queue
# (3) Display the waiting list
# Implement record as a list containing following fields.
# Waiting_no   			Integer
# Passenger_name 		String
# Passenger_age			Integer
