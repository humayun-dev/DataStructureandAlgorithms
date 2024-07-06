'''
    Linear probing implementation is through dictionary in Python and there should be two arrays such as one array for the 
    key/slot and another array is for the data
'''
class dictionary:
    def __init__(self,size):
        self.size = size
        self.slot = [None] * self.size      # key/slot array
        self.data = [None] * self.size      # data array
    
    # to insert the data into the specified location
    def put(self,key,value):
        hash_value = self.hash_function(key)

        # what if there isn't any value then
        if self.slot[hash_value] == None:
            self.slot[hash_value] = key
            self.data[hash_value] = value
        else:
            # slot is not empty but already there is the same value so
            if self.slot[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)    # rehash value assign to the new hash value
                # but what even the new hash value is not empty then go for loop and find empty plus shouldn't be duplicate value
                while self.slot[new_hash_value] != None and self.slot[new_hash_value] != key:  
                    new_hash_value = self.rehash[new_hash_value]
                
                if self.slot[new_hash_value] == None:
                    self.slot[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value
    
    # rehash for the put function when there is already a key on a specified location so to place in the next slot
    def rehash(self,old_hash):
        return (old_hash + 1) % self.size

    # calculate hash value before insertion into array 
    def hash_function(self,key):
        return abs(hash(key)) % self.size
    
    # fetch items from the dictionary
    def get(self,key):
        start_position = self.hash_function(key)
        current_position = start_position
        while self.slot[current_position] != None:

            if self.slot[current_position] == key:
                return self.data[current_position]
            
            current_position = self.rehash(current_position)

            if current_position == start_position:
                return "Not found"
        
        return "Not found"

# create the dictionary/object
d = dictionary(3)   # 3 items
print(d.slot)       # at this stage = None 3 times
print(d.data)       # at this stage = None 3 times

d.put("first",1)
print(d.slot)
print(d.data)

d.put("second",2)
print(d.slot)
print(d.data)

# fetch data
print(d.get("first"))
print(d.get("second"))
print(d.get("404"))        # not found fetch