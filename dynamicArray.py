''' 
    1. Creating Dynamic Array
    2. Length of the list
    3. Append the list items
    4. Print the list
    5. Accessing elements via index
'''
import ctypes

# 1. Creating Dynamic Array
class DynamicArray:
    def __init__(self):
        self.size = 1
        self.n = 0          # input = 0
        # create a C type array with size = self.size
        self.A = self.make_array(self.size)
    
    def make_array(self, capacity):
        # create a C type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()
    
    # 2. Length of the list
    def __len__(self):
        return self.n
    
    # 3. Append the list items
    def append(self, item):
        if self.n == self.size:
            # if there isn't any space then resize
            self.resize(self.size * 2)
        # if space exists then append
        self.A[self.n] = item
        self.n += 1
    
    # Resize function
    def resize(self, new_capacity):
        # create new array with new capacity
        B = self.make_array(new_capacity)
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B
        self.size = new_capacity
    
    # 4. Print the list
    def __str__(self):
        result = ', '.join(str(self.A[i]) for i in range(self.n))
        return '[' + result + ']'

    # 5. Accessing elements using index
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            raise IndexError('Index error: out of bound')

# 1. Create object of the above list which is part of the class DynamicArray
obj = DynamicArray()
print(type(obj))   # to check the data type of the list
print()

# 2. Length of the list
print(len(obj))  # Output: 0

# 3. Append the items
obj.append("hello")
obj.append(3)
obj.append(4.4)
print(len(obj))  # Output: 3

# 4. Print the list
print(obj)  # Output: [hello, 3, 4.4]

# 5. Accessing elements via index
print(obj[2])  # Output: 4.4

# Uncommenting the following line will raise IndexError
# print(obj[5])  # IndexError: Index error: out of bound
