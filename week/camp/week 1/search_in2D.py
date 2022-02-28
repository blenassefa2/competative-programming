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
            return True
    return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) -1
        best = 0

        while top <= bottom:
            median = int(top + (bottom -top)/2)

            if matrix[median][0] > target:
                bottom = median - 1
            else:
                best = median
                top = median + 1
            
        return binary_search(target,matrix[best])
        