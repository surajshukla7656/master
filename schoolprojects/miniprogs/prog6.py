# python program to write a random number generator that generates random numbers between 1 and 6(simulates a dice)

import random

# dice
def dice_rolls():

    return random.randint(1,6)

# main
def main():

    print('r or R to roll dice and e for exit')

    while True:

        dec=input('>>> ')

        if dec=='e':

            break
            
        elif dec=='r' or dec=='R':

            print(dice_rolls())

        else:

            print('invalid input')

# driver's code
if __name__=='__main__':
    main()