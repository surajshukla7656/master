# python program to write a random number generator that generates random 
# numbers between 1 and 6

from random import randrange

def random_number_generator():
    print('e or E for exit ')
    while True:

        print(randrange(1,7))
        prompt=input('>>> ')
        if prompt in ('e','E'):
            print('bye')
            break


if __name__=='__main__':
    
    random_number_generator()


