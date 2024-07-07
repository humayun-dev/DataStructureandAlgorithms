'''
    Searching and sorting algorithms
    1. Linear search (compare the given item with all the array elements)
    2. Binary search (needs sorted array, search based on dividing the array items)
'''
# Linear search
def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = [1,2,3,4,5,150,250,350,50,25,30]
print(linear_search(arr,50))  # search 50 in the array

# Binary search
# in binary search the check for the middle item is must and it can be found as (lowest index + highest index) // 2
def binary_search(arr,low,high,item):
    if low <= high:
        mid = (low + high) // 2     # integer conversion
        if arr[mid] == item:        # if mid = item then return mid and stop rest code execution
            return mid
        elif arr[mid] > item:       # if mid value is greater than the item value
            return binary_search(arr,low,mid-1,item)    # high is updated to the mid - 1 value
        else:
            return binary_search(arr,mid+1,high,item)   # low is updated to the mid + 1 value
    else:
        return -1

arr = [1,2,3,4,5,150,250,350,400,500,600,750,800]
print(binary_search(arr,0,len(arr),250))