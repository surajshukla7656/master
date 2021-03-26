# python program to implement stack using list

# checking whether the stack is empty or not
def isempty(stack):
    if len(stack)==0:
        return True

    else:
        return False


# adding new element into the stack
def push(stack,item):
    stack.append(item)
    print('new item added')



# removing the element
def pop(stack):
    if isempty(stack)==True:
        print('stack is empty')
    else:
        stack.pop()
        print('poped')


# top element
def top(stack):
    if isempty(stack)==True:
        print('stack is empty')

    else:
        print('top element :',stack[-1])

# size of stack
def size(stack):

    print('size of stack :',len(stack))

# display
def display(stack):
    if isempty(stack)==True:
        print('stack is empty')
    
    else:
        for element in stack[::-1]:
            print(element)


# driver's code
if __name__=='__main__':
    l=[2,4,6,8,10]
    print(isempty(l))
    push(l,4)
    display(l)
    pop(l)
    display(l)
    top(l)
    size(l)

