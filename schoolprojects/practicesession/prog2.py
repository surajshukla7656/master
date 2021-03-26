# python program to read a textfile and display the number of 
# vowels,consonants,uppercase,lowercase characters in the file

def main():

    with open('textfile2.txt','r') as f:

        countV=countC=countU=countL=0

        for char in f.read():
            
            if char.isalpha():
                if char in ('a','A  ','e','E','i','I','o','O','u','U'):
                    countV+=1

                else:
                    countC+=1
                
                if char.isupper():
                    countU+=1
                    
                else :
                    countL+=1

        print('no of vowels : ',countV)
        print('no of consonants : ',countC)
        print('no of uppercase : ',countU)
        print('no of lowercase : ',countL)

if __name__=='__main__':

    main()
                
