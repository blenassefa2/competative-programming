def possible(arr,d,c):
    left = 0
    right = 0
    days = [0]*d
    sum_ = 0
    i = 0
    while i <d and right <len(arr):
        while right <len(arr) and days[i] + arr[right] <= c:
            days[i] += arr[right]
            right += 1
        i+=1
   
    if sum(days) < sum(arr):
        return False
            
        
        
    return True
    
            
            
    
    
    
    # if arr and d == 0:
    #     return False
    # elif not arr and d >= 0:
    #     return True
    # x = 0
    # sum_ = 0
    # i = 0
    # while i <len(arr):
    #     if sum_ < c:
    #         sum_ += arr[i]
    #         i += 1
    #         continue
    #     return possible(arr[i+1:],d-1,c)
        
        
        
            
    
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)
        best = 0
        while left <= right:
            median = int(left + (right - left)/2)
            p =  possible(weights,days,median)
          
            if not p:
                left = median + 1
            else:
                best = median
                right = median - 1
        return best
            