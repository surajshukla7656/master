f=open('/home/surajshukla7656/Documents/nextpython/file.txt')
chat=f.readlines()
count=0
while True:
    noOfLine=int(input("Enter no of lines:"))
    noOfLines=noOfLine-count
    whattodo=input("s for skip and a for append:")
    if whattodo=="s":
        count+=noOfLines
    else:
        filename=input("enter filename:")
        for i in range(noOfLines):
            x=open(f"{filename}.py","a")
            x.write(chat[count])
            count+=1
        print(f"successfully written in file {filename}")
        print(f.tell())

        

 