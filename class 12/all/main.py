

f=open("/home/surajshukla7656/Downloads/chat1.txt")
chat=f.readlines()
for  i in chat:
    for j in i:
        if j.isdigit()==True or j=="?" or j=="P":
            break
        else:
            x=open("file.txt","a")
            x.write(i) 
            break