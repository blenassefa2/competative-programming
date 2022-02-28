
    
def Less_num(r,c,x):
    j = 0
    max_ =0
    if r >= c:
        j = c
        max_ = r
    else:
        j = r
        max_ = c
    result = 0
    for i in range(1,j+1):
        result += min(max_, x //i)
    return result
        
    
    
    
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m*n
        best = -1
        while left <=right:
            mid = int(left +(right-left)/2)
            nums = Less_num(m,n,mid)
             
            
            if nums < k:
                
                left = mid + 1
            else:
                best = mid
                right = mid -1
            
        return best
                
                
            
        
        