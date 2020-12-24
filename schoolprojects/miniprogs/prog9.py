# python program to find most recurring emails/words
import sys

# main
def main(file):

    with open(file,'r') as f:

        file_content=f.read().upper().split()

    element_dict={}

    for element in file_content:

        if element in element_dict:

            element_dict[element]+=1

        else :

            element_dict[element]=1

    element=max(element_dict.values())

    print('Most recurring Words')

    for key,value in element_dict.items():

        if value==element:

            print(key,'-',value)

# driver's code
if __name__=='__main__':

    file=sys.argv[1]

    main(file)