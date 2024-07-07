'''
    Searching and sorting algorithms
    1. Linear search (compare the given item with all the array elements)
    2. Binary search (needs sorted array, search based on dividing the array items)
    3. Bubble sorting (comparison of the array elements and least value to the least index placement)
    4. Selection sorting (sort the unsorted array)
    5. Merge sorting
    6. Quick sorting
    7. Insertion sort
'''
# 1.Linear search
def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = [1,2,3,4,5,150,250,350,50,25,30]
print(linear_search(arr,50))  # search 50 in the array

# 2.Binary search
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
print(binary_search(arr,0,len(arr)-1,250))

# 3.Bubble sort
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]       # a = 2, b = 3, a,b = b,a (swapping in python)
    print(arr)

arr = [5,3,4,2,1,6,79,80]
print("Before bubble sort: ")
for i in range(len(arr)):
    print(arr[i],end=' ')
print("\nAfter Bubble Sort ")
bubble_sort(arr)

# 4.Selection sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print(arr)

arr = [5,3,4,2,1,6,79,80]
print("Before selection sort: ")
for i in range(len(arr)):
    print(arr[i],end=' ')
print("\nAfter selection Sort ")
selection_sort(arr)