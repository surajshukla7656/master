#python program to read a text file line by line and display each word separated by a '#'

import sys

# main
def main(file):

    with open(file,'r') as f:

        for line in f.readlines():

            newline=line.replace(' ','#')

            print(newline,end='')

        print()

# driver's code
if __name__=='__main__':

    file=sys.argv[1]

    main(file)

