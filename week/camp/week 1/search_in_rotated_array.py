class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                break
            i += 1
        if target == nums[i]:
            return i
        elif nums[0] <= target:
            l = 0
            r = i
        else:
            l = i + 1
            r = len(nums) - 1
        index = - 1 
        
        while l <= r:
            
            mid = int((l + r) / 2)
            
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r  = mid - 1
            else:
                index = mid
                return index
                break
                
        return -1