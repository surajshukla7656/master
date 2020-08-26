for x in range(len(stack)):
    print(stack[len(stack) - x - 1 ])


  
# pop() fucntion to pop 
# element from stack in  
# LIFO order 
print('\nElements poped from stack:') 
print(stack.pop()) 

print('\nStack after some elements are poped:') 
for x in range(len(stack)):
    print(stack[len(stack) - x - 1 ])
print()
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
for x in range(len(stack)):
    print(stack[len(stack) - x - 1 ])
  
# uncommenting 
print(stack.pop())   
# will cause an IndexError  
# as the stack is now empty
# using list

# Check whether the stack is empty
def isStackEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

# Push item on to the stack   
def push(stack, item):
    stack.append(item)

# Pop itemfrom the stack
def pop(stack):
    if isStackEmpty(stack):
        print("Stack is empty")
    else:
        item = stack.pop()
        print("The element popped: " + str(item))

# Display the contents of the stack
def display(stack):
    if isStackEmpty(stack):
        print("Stack is empty")
    else:
        top = len(stack) - 1
        for i in range(top, -1, -1):
            print(stack[i])
# Display the element of the top of the stack
def top(stack):
    if isStackEmpty(stack):
        print("Stack is empty")
    else:
        print("The element of the top of the stack: " + str(stack[-1]))

# Executable code
if __name__ == "__main__":
    s = []
    display(s)

    push(s, 11)
    push(s, 22)
    push(s, 33)
    push(s, 44)
    top(s)
    display(s)

    pop(s)
    pop(s)
    display(s)

    pop(s)
    top(s)
    pop(s)
    pop(s)


Run and Output:
$ python stack.py
Stack is empty
The element of the top of the stack: 44
The element popped: 44
The element popped: 33
The element popped: 22
The element of the top of the stack: 11
The element popped: 11
Stack is empty
# demonstrate queue implementation 
# using list 
  
