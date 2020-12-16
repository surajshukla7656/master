# python program to implement stack using a list data-structure


# check whether  a stack is empty or not
def isempty(stack):

    if len(stack)==0:

        return True
    
    else :

        return False
    
# to pop an element from the stack
def pop(stack):

    if isempty(stack)==True:

        print('Empty Stack\n')

    else :

        print('Element popped-{}\n'.format(stack.pop()))

# to push an element in the stack
def push(stack,item):

    stack.append(item)

    print('Appended new element - {}\n'.format(item))

# to get the size of stack
def size(stack):

    print('size of stack : {}\n'.format(len(stack)))

# to get the top element of stack
def top(stack):

    if isempty==True:

        print('Empty Stack\n')

    else:

        print('top element of stack : {}\n'.format(stack[-1]))

def display(stack):

    if isempty(stack)==True:

        print('Empty Stack\n')

    else :

        front_end=len(stack)-1

        print('Elements of stack\n')
        for element in range(front_end,-1,-1):

            print(stack[element])

# driver's code
if __name__=='__main__':

    l=[x for x in range(1,11)]

    display(l)

    pop(l)

    display(l)

    top(l)

    push(l,4)

    display(l)
    
    size(l)