from math import ceil


def binary_search(val,arr):
    left = 0
    right = len(arr) -1
   
    while left <= right:
        median = int(left + (right -left)/2)
       
        if arr[median] < val:
            left = median + 1
        elif arr[median] > val:
            right = median - 1
        else:
            return median
    return -1
def interval_search(val, arr):
    first= len(arr)
    last = -1
    left = 0
    right = len(arr) -1
    while left <= right:
        median = int(left + (right -left)/2)
       
        if arr[median] < val:
            left = median + 1
        elif arr[median] > val:
            right = median - 1
        else:
            if median >last:
                last = median
            else:
                if median < first:
                    first = median
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binary_search(target,nums))
target = 89
print(binary_search(target,nums))
target = -1
print(binary_search(target,nums))
