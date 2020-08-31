import random
import time
import os

data = [0 for i in range(9)]
str1 = [" " for i in range(9)]

def makestring() :
    
    
    
    for index , element in enumerate(data) :
        
        if element == 1 and str1[index] == " " :
            
            str1[index] = "X"
            
        elif element == -1 and str1[index] == " " :
            
            str1[index] = "O"
            
        elif element == 1 and str1[index] == "O" :
            
            print('\033[91m' + "Invalid Move" + '\033[0m')
            data[index] = -1
            
            makestring()
            playersturn()
            
    n = 1
    
    for i in range(9) :
        
        if n % 3 == 0 :
            
            print(str1[i] , end = "\t")
            print()
            
            
            n += 1
            
        else :
            
            print(str1[i] , end = "\t")
            
            n += 1
            
            
def compturn() :
    
    os.system("clear")
    
    available = []
    
    for i in range(9) :
        
        if data[i] == 0 :
            
            available += [i]
            
    move = random.choice(available)
    
    data[move] = -1
    
    makestring()
    
    isWin(caller = -1)
    
    
def playersturn() :
    
    index = int(input("Enter The Move [1~9] :\t")) - 1
    
    data[index] = 1
    os.system("clear")
    makestring()
    isWin(caller = 1)
    
    time.sleep(1)

# Checks if someone won 
# @arguments : caller (1 : for player and -1 : computer)    
def isWin(caller) :
    
    def killzero(number) :
        
        for index , element in enumerate(data) :
            
            if element == 0 :
                
                data[index] = number
    
    winmove = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    
        
    if data.count(caller) >= 3 :
            
            moves = tuple()
            
            for index , element in enumerate(data) :
                
                if element == caller :
                    
                    moves += (index , )
            
            for i in winmove :
                
                if ( ( i[0] in moves ) and ( i[1] in moves ) and ( i[2] in moves ) ) :
                    
                    if caller == 1 :
                    
                        print('\033[92m' + "You Won")
                    
                        killzero(1)
                    
                    else :
                        
                        print('\033[92m' + "Computer Won")
                        
                        killzero(-1)
        
    
    
def main() :
    
    while 0 in data :
        
        playersturn()
        
        if 0 in data :
            compturn()  
        
        
if __name__ == "__main__" :
    
    main()