'''
    A stack is a data structure having concept of Last In First Out (LIFO). The main concepts of the stack are 
    push, pop, size, peek, empty, top.
    The top is the head item while peek is the last item of the stack
'''

# Node class for the stack
class node:
    def __init__(self,value):
        self.data = value
        self.next = None

# stack class
class stack:
    def __init__(self):
        self.top = None     # top = head and by default its value is empty
    
    # when stack is empty
    def isempty(self):
        return self.top == None
    
    # push items in the stack
    def push(self,value):
        newNode = node(value)
        newNode.next = self.top
        self.top = newNode
    
    # traverse the stack
    def traverse(self):
        current = self.top
        while current != None:
            print(current.data)
            current = current.next

    # returning peek item of the stack
    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return print(self.top.data)
    
    # pop item from the stack
    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            self.top = self.top.next
    
    # Get the size of the stack
    def size(self):
        current = self.top
        count = 0
        while current != None:
            count += 1
            current = current.next
        return print(count)
        
# creating object/stack
s = stack()
print(s.isempty())     # it should return true in this case

for i in range(5):
    s.push(i)

s.traverse()            # display the stack items

s.peek()                # return peek item of the stack

#s.pop()                 # pop one item from the stack
#s.traverse()

s.size()                # return size of the stack