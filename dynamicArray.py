''' 
    1. Creating Dynamic Array
    2. 
'''
import ctypes

# 1.Creating Dynamic Array
class DynamicArray:
    def __init__(self):
        self.size = 1
        self.n = 0          # input = 0
        # create a C type array with size = self.size
        self.A = self.makeArray(self.size)
    
    def makeArray(self,capacity):
        # create a C type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()
    
    # 2.length of the list
    def __len__(self):
        return self.n
    
    # 3.append the list items
    def __append__(self,item):
        if self.n == self.size:
            # if there isn't any space then resize
            self.__resize(self.size * 2)
        # if space exists then append
        self.A[self.n] = item
        self.n = self.n + 1 
    
    # resize function
    def __resize(self,new_capacity):
        # create new array with new capacity
        B = self.makeArray(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

# 1.create object of the above list which is part of the class DynamicArray
obj = DynamicArray()
print(type(obj))   # to check the data type of the list
print("\n")
print(obj)  # it will print the address of the object

# 2.length of the list
print(len(obj))

# 3.append the items
obj.__append__("hello")
obj.__append__(3)
print(len(obj))
