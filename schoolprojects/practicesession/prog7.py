# python program to implement stack using a list data-structure


# check whether a stack is empty or not
def isempty(stack):
    if len(stack)==0:
        return True
    else:
        return False

# returning size of stack
def size(stack):
    print(len(stack))

# adding data
def push(stack,item):
    stack.append(item)

# removing data
def pop(stack):
    if isempty(stack)==True:
        print('stack is empty')


    else:
        stack.pop()
        print('item removed')

# top element
def top(stack):
    if isempty(stack)==True:
        print('stack is empty')

    else:
        print(stack[-1])

