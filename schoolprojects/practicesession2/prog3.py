# python program to read a file name
# and perform counting

with open('textfile3','r') as f:

    file_content=f.read()

    countA=countU=countL=countD=countW=countS=0

    for char in file_content:

        if char.isalpha():
            countA+=1
            if char.isupper():
                countU+=1
            
            else:
                countL+=1

        elif char.isdigit():
            countD+=1

        elif char.isspace():
            countW+=1

        else :
            countS+=1

print('total number of characters :',len(file_content))
print('total number of alphabets :',countA)
print('total number of Uppercase characters :',countU)
print('total number of Lowercase characters :',countL)
print('total number of digits :',countD)
print('total number of white spaces :',countW)
print('total number of special characters :',countS)

