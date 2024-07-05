'''
    A linked list is a collection of nodes, linear data structure and best use when we have heavy write instead of heavy read
    It consists of a node and node is basically an object having two parts such as data and address

    1. Creating node class and a linked list class
    2. length of the linked list
    3. Insert from the head (the first node is called head)
    4. Traversing or printing the nodes
    5. Insert from tail(append)
    6. Insert value to a given position
    7. Delete from head
    8. Delete from tail (pop)
    9. Delete by value (remove)
    10. Search by value 
    11. Delete by index 
    12. Search by index
'''
# 1. Creating node class and a linked list class
class node:
    def __init__(self,value):
        self.data = value
        self.next = None

class linkedList:
    def __init__(self):
        # when linked list is empty
        self.head = None    # first node is always head and is None
        self.n = 0          # no of nodes always 0 when empty

    # 2. length of the linked list
    def __len__(self):
        return self.n
    
    # 3.Insert from the head (the first node is called head)
    def insertNode(self,value):
        newNode = node(value)           # create new node
        newNode.next = self.head        # create connection for the head
        self.head = newNode             # update the head node
        self.n = self.n + 1             # increment the linked list
    
    # 4.Traversing or printing the nodes
    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data) + '->'
            current = current.next
        
        return result[:-2]

    # 5.Insert from tail(append)
    def append_at_end(self,value):
        newNode = node(value)       # create the new node
        if self.head == None:       # what if the list is empty
            self.head = newNode
            self.n = self.n + 1
            return
        
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = newNode
        self.n = self.n + 1

    # 6.Insert value to a given position
    def insert_into_position(self,position,value):
        newNode = node(value)
        current = self.head

        while current != None:      # loop to find the specified position
            if current.data == position:
                break
            current = current.next
        
        # Case 1: when item found
        if current != None:
            newNode.next = current.next
            current.next = newNode
            self.n = self.n + 1
        # Case 2: when item not found
        else:
            print("Item not found") 

# create object of the linked list class
L = linkedList()
print(L)
print(len(L))   # print the length of the linked list

L.insertNode(1)     # insert the nodes
L.insertNode(2)
L.insertNode(3)
L.insertNode(4)
L.insertNode(5)

print(L)            
print(len(L))       # linked list updated

print(L)            # display of the linked list items

L.append_at_end(6)  # inserting node at the end
print(L)

L.insert_into_position(4,400)       # insert 400 after 4 in the list
print(L)
L.insert_into_position(600,2)       # item not found in the list