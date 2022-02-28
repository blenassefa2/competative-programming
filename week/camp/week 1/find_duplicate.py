class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        
        while start <= end:
            mid = int((start + end)/2)
            x = 0
            for i in range(len(nums)): 
                if nums[i] <= mid:
                    x+=1
                    
            if x <= mid:
                start = mid + 1
            else: 
                best = mid
                end = mid - 1
                
            
        return best