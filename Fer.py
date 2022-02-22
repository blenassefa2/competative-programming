def left(i):
    return (2*i)+1
def right(i):
    return (2*i)+2
def maxChild(arr,n, i):
    if right(i) > n:
        return left(i)
    if arr[left(i)] < arr[right(i)]:
        return right(i)
    return left(i)
def parent(i):
    if i% 2 == 0:
        return (i -2)//2
    return (i - 1) // 2
def getMAx(arr):
    return arr[0]
def isLeaf(index,arr):
    if (2*index) + 1 >= len(arr) or (2*index) + 2 >= len(arr):
        return True
    return False

def moveUp(arr, n, i):
    while i > 0 and arr[i] > arr[parent(i)]:
        arr[i], arr[parent(i)] = arr[parent(i)],arr[i]
        i = parent(i)
def moveDown(arr, n, i):
    
    while not isLeaf(i,arr) and maxChild(arr,n,i) < n and arr[i] < arr[maxChild(arr,n,i)]:
        arr[i], arr[maxChild(arr,n,i)] = arr[maxChild(arr,n,i)],arr[i]
        i = maxChild(arr,n,i)

def heapify( arr, n, i):
    moveUp(arr,n,i)
    moveDown(i,arr,n)

def buildHeap(arr,n):
    for i in range(n):
        moveUp(arr,n,i)

def heapSort(arr,n):
    buildHeap(arr, len(arr))
    print(arr)
    while n > 0:
        arr[0],arr[n-1] = arr[n-1],arr[0]
        moveDown(arr,n-1,0)
        n-=1
    
arr = [3,4,5,2,0]
heapSort(arr,len(arr))
# moveDown(arr,len(arr),0)
print(arr)