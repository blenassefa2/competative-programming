"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for i in range(1,1001):
            left = 1
            right = 1001
            
            while left <= right:
                mid = int(left + (right- left)/2)
                x = customfunction.f(i,mid)
                if x > z:
                    right = mid -1
                elif x < z:
                    left = mid +1
                elif x== z:
                    ans.append([i,mid])
                    break
        return ans
                
            
        