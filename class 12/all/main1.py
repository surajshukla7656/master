
f=open('/home/surajshukla7656/Documents/nextpython/file2.py')
chat=f.readlines()

for i in chat:
    print(i)
    a=input(">>>")
    if a=="n":
        filename=input("enter filename:")
        x=open(f'{filename}.py',"a")
        x.write(i)
        
    elif a=="a":
       x=open(f'{filename}.py',"a")
       x.write(i)

    else :
       pass
        