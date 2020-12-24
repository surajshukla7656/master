# python program to implement queue using a list

# check whether a queue is empty or not
def isempty(stack):

    if len(stack)==0:

        return True

    else :

        return False

# enqueue an element in the queue

def enqueue(queue,item):

    queue.append(item)

    print('New Element {} Added\n'.format(item))

# dequeue an element from the queue

def dequeue(queue):

    if isempty(queue)==True:

        print('Empty queue\n')

    else:

        print('dequeued {}\n'.format(queue.pop(0)))


# size of the queue

def size(queue):

    print('Size of queue : {}\n'.format(len(queue)))

# display

def display(queue):

    if isempty(queue):

        print('Empty Queue\n')

    else:

        front_end=0

        rear_end=len(queue)-1

        print('Elements of queue :')

        for element in range(front_end,rear_end):

            print(element)


# rear end

def rear_end(queue):

    print('Rear end : {}\n'.format(queue[-1]))

# front end

def front_end(queue):

    print('Front end : {}\n'.format(queue[0]))

# driver's code
if __name__=='__main__':

    l=[x for x in range(1,11)]

    display(l)

    enqueue(l,30)

    display(l)

    dequeue(l)

    display(l)

    size(l)

    rear_end(l)

    front_end(l)