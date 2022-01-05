class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        final = []
        count = 0
        for i in range(len(nums)):
            
            if i ==0:
                final .append(nums[i])
                continue
                
            if nums[i] <= final[-1]:
                x = final[-1] 
                x += 1
                final.append(x)
                count = count +( final[-1] - nums[i])                
               
            else:
                final.append(nums[i])
        return count