# Stack implementation
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
if _name_ == "_main_":
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



# Queue implementation
# using list and functions

# Check whether the queue is empty
def isQueueEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

# Insert an element at the rear end of the queue
def enqueue(queue, item):
    queue.append(item)

# Delete an element from the front of the queue
def dequeue(queue):
    if isQueueEmpty(queue):
        print("Queue is empty")
    else:
        item = queue.pop(0)
        print("The element deleted from the queue: " + str(item))
    
# Display the contents of the queue
def display(queue):
    if isQueueEmpty(queue):
        print("Queue is empty")
    else:
        front = 0
        rear = len(queue) - 1
        print("\nThe elements in the queue are:")
        for i in range(front, rear + 1):
            print(queue[i], end = ' ')
        print()

# Executable code
if _name_ == "_main_":
    Q = []
    display(Q)

    enqueue(Q, 9)
    enqueue(Q, 18)
    enqueue(Q, 27)
    enqueue(Q, 36)
    enqueue(Q, 45)

    display(Q)

    dequeue(Q)
    dequeue(Q)

    display(Q)

    dequeue(Q)
    dequeue(Q)
    dequeue(Q)
    dequeue(Q)