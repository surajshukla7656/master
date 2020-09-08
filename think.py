from itertools import chain, combinations
from statistics import mode

winmove = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 4, 8}, {2, 4, 6}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8})

def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = iterable
    x = tuple(chain.from_iterable(combinations(s, r) for r in range(2 , 3)))
    
    y = tuple()
    
    for i in x :
        
        y += (set(i), )
        
    return y

# Returns the moves till now used by one of the two players
# @arguments : calledFor : (1 : for player \and -1: for computer)
#                            data : record of moves till now by both
def moves(calledFor , data) :
    
    if data.count(calledFor) >= 2 :
            
            moves = tuple()
            
            for index , element in enumerate(data) :
                
                if element == calledFor :
                    
                    moves += (index , )
                    
            return moves
    
    else :
        
        return None
        
        
def think(data , calledFor) :
    
    cmove = moves(calledFor , data)
    if not (cmove == None) :
        
        possibleMovesOpponent = powerset(cmove)
        
        #checking every possible move via which one can win in current situation
        mymove = tuple()
        
        for turn in winmove :
            
            for possibility in possibleMovesOpponent :
                
                if possibility.issubset(turn) and data[tuple(turn - possibility)[0]] == 0 :
                    
                    mymove += tuple(turn - possibility)
        
        return mymove
            

def compthink(data) :
    
    m1 = think(data , calledFor = -1)
    
    if m1 != None :
        if len(m1) > 0 :
        
            todo = mode(m1)
            return todo
        
    else :
        
        m1 = think(data , calledFor = 1)
        
        if m1 != None :
            if len(m1) > 0 :
                todo = mode(m1)
                return todo
        
        else :
            
            return None



