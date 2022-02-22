
def parent(i):
        if i% 2 == 0:
            return (i -2)//2
        return (i - 1) // 2
def moveUp( arr, n, i):
    while i > 0 and arr[i] < arr[parent(i)]:
        arr[i], arr[parent(i)] = arr[parent(i)],arr[i]
        i = parent(i)
def left( i):
        return (2*i)+1
def isLeaf(index,arr):
    if (2*index) + 1 >= len(arr) or (2*index) + 2 >= len(arr):
        return True
    return False
def right( i):
    return (2*i)+2
def moveDown(index,arr,n):
    
    if isLeaf(index,arr) or (arr[index] < arr[left(index)] and arr[index] <  arr[right(index)]) :
        return
    min_ = -1
    if left(index) < n:
        min_ =  left(index)
    
    if right(index) < n and right(index)<len(arr) and arr[ right(index)] < arr[min_]:
        min_ =  right(index)
    if min_ != -1 and arr[min_] < arr[index]:
        arr[min_] , arr[index] = arr[index] , arr[min_]
        moveDown(min_,arr,n)
        
    
def heapify( arr, n, i):
        moveUp(arr,n,i)
        moveDown(i,arr,n)
def insert( arr, val):
    arr.append(val)
    moveUp(arr,len(arr),len(arr)-1)
def buildHeap(arr,n):
    for i in range(n):
        moveUp(arr,n,i)

def heapSort(arr,n):
    buildHeap(arr, len(arr))
    print(arr)
    while n > 0:
        arr[0],arr[n-1] = arr[n-1],arr[0]
        moveDown(0,arr,n-1)
        n-=1
    
arr= [0,1,2,3,4,5,6,7,8,9,10,3435]
# for i in range(len(arr)):
#     arr[i] *= -1
# print(arr)
heapSort(arr,len(arr))
# print(arr)
# for i in range(len(arr)):
#     arr[i] *= -1
print(arr)