            #checking the keys of input data
            if str(item.keys())!="dict_keys(['member_no', 'member_name', 'age'])":
                raise KeyError("only member_no  , member_name , age are allowed")

            #checking the data type of values
            elif type(item["member_no"])!=int or type(item["member_name"])!=str or type(item["age"])!=int:
                raise TypeError("you have enetered wrong data type")

            #appending new input data into the queue instance
            else:
                self.append(item)
            
        #if the item is list then converting it into dict data type 
        elif type(item)==list and len(item)==3:
            #checking the  data types of input values
            if type(item[0])!=int and  str(item[0]).isdigit()==False or type(item[2])!=int or str(item[2]).isdigit()==False:
                raise TypeError("only int is allowed")

            elif type(item[1])!=str:
                raise TypeError("only string is allowed")

            #appending the new data type into the  queue instance
            else:
                dict_item={
                    "member_no":int(item[0]),
                    "member_name":str(item[1]),
                    "age":int(item[2])
                }
                self.append(dict_item)
        else:
            raise TypeError("You have entered wrong data type")

    #delete a value from the top end of the queue
    def Dequeue(self):
        if self.IsQueueEmpty()=="IsEmpty":
            raise ValueError("Empty queue")
        else:
            return self.pop(0)
    
    #display the items of the queue
    def display(self):
        if self.IsQueueEmpty()=="IsEmpty":
            print("EmptyQueueInstance")
        else:
            front=0                #index of front end of the instance
            rear=len(self)-1       #index of rear end of the instance
            
            print("---------------------------front end----------------------------")

            for item in range(front,rear+1):

                print(f'''member no:{self[item]["member_no"]}
member name :{self[item]["member_name"]}
age:{self[item]["age"]}''')

                print()
                print()

            print("---------------------------rear end----------------------------")
            print()
            print()
 
    #Prevention of insertion of the item in the middle of the queue
    def insert(self,item):
        raise AttributeError("you can't insert any item in the middle of a queue instance")


#driver's code
if __name__=="__main__":

    q1=Queue()
    q1.Enqueue([6,"kuldeep",16])
    q1.Enqueue([5,"surajshukla",18])
    q1.display()

    q1.Dequeue()
    q1.display()
    
    q1.Enqueue({"member_no":4,"member_name":"suraj","age":4})
    q1.display()
member no:6
member name :kuldeep
age:16


member no:5
member name :surajshukla
age:18


---------------------------rear end----------------------------


