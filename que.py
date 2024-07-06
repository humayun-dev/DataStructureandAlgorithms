'''
    A queue is a data structure that has concept as First In First Out (FIFO). The insertion is called enqueue and that will be
    at the end of the queue. While the deletion is called dequeue and that is removed element from the front of the queue.
    The main concepts are enqueue, dequeue, front(get element at the front of the queue without removing), rear(opp of the front),
    isEmpty and size
'''
# node class for the queue
class node:
    def __init__(self,value):
        self.data = value
        self.next = None

# queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear =  None
    
    # enqueue to the queue
    def enqueue(self,value):
        newNode = node(value)
        if self.rear == None:
            self.front = newNode
            self.rear = self.front
        else:
            self.rear.next = newNode
            self.rear = newNode
    
    # dequeue to the queue
    def dequeue(self):
        if self.rear == None:
            return "Empty Queue"
        else:
            self.front = self.front.next
    
    # traverse the queue
    def traverse(self):
        current = self.front
        while current != None:
            print(current.data)
            current = current.next

# create object/queue
q = Queue()

# enqueue the items
for i in range(5):
    q.enqueue(i)

# show the items
q.traverse()

# dequeue an item
q.dequeue()
q.traverse()


