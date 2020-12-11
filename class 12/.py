
# q-31
def Display(str):
    m=""
    for i in range(0,len(str)):
        if(str[i].isupper()):
            m=m+str[i].lower()
        elif str[i].islower():
            m=m+str[i].upper()
        else:
            if i%2==0:
                m=m+str[i-1]
            else:
                m=m+"#"
    print(m)

Display('Fun@Python3.0')

# q-34
def LShift(ARR,n):

    n=n%len(ARR)

    ARR=ARR[n:]+ARR[:n]

    print(ARR)

l=[10,20,30,40,50,60,70]

LShift(l,2)


# q-35
def Count():

    with open('nextpython/STORY.TXT','r') as f:

        file_content=f.read()

        file_content=file_content.lower()

        l=file_content.split()

        a=l.count('me')

        b=l.count('my')

        print('Total me and my are',a+b)

# q-35
def  AMCount():

    with open('nextpython/STORY.TXT','r') as f:

        countA=countM=0

        for char in f.read():

            if char=='a' or char=='A' :

                countA+=1
            
            elif char=='M' or char=='m':

                countM+=1

    print('A or a:',countA)

    print('M or m:',countM)

AMcount()