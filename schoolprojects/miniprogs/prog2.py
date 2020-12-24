# python program to read a text file and display the number of vowels,consonants,uppercase,lowercase characters in the file

import sys

# main
def main(file):

    with open(file,'r') as f:

        vowels=['a','e','i','o','u']

        countup=countlow=countvow=0
        
        for char in f.read():

            if char.isalpha() :

                if char.isupper() :

                    countup+=1

                else:
                    
                    countlow+=1

                if char in vowels:
                    
                    countvow+=1
        

    print('no of consonants : {}'.format(countup+countlow-countlow))
    print('no of vowels : {}'.format(countvow))
    print('no of uppercase characters : {}'.format(countup))
    print('no of lowercase characters : {}'.format(countlow))


# driver's code 
if __name__=='__main__':

    file=sys.argv[1]

    main(file)
