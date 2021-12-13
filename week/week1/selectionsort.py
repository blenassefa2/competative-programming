class Solution: 
    def select(self, arr, i):
        # code here
        minimum = arr[i] 
        index = 0
        for n in range(i,len(arr)):
            if minimum>=arr[n]:
                minimum = arr[n]
                index = n
        return index
    
    def selectionSort(self, arr,n):
        
        for i in range(0,n):
            j = self.select(arr,i)
            arr[i], 