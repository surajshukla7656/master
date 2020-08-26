  
# Removing elements from the queue 
print("\nElements dequeued from queue") 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 
  
print("\nQueue after removing elements") 
print(queue) 
  
# Uncommenting print(queue.pop(0)) 
# will raise and IndexError 
# as the queue is now empty 


Run and Output:
$ python queue1.py
Initial queue
['a', 'b', 'c']

Elements dequeued from queue
a
b
c

Queue after removing elements
[]
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

        for i in range(front, rear + 1):
            print(queue[i], end = ' ')
        print()

# Executable code
if __name__ == "__main__":
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

Run and Output:
$ python queue.py
Queue is empty
The element deleted from the queue: 9
The element deleted from the queue: 18
The element deleted from the queue: 27
The element deleted from the queue: 36
The element deleted from the queue: 45
Queue is empty
enqueue(queue, item), dequeue(queue) and display(queue)
The item contains the following fields:
member_no	integer
member_name	string
