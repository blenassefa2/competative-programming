class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        best = -1
        last = -1
        l = 0
        r = len(nums) - 1
        b_nums = [i for i in nums]
        l_nums = [i for i in nums]
        while l <= r:
            mid_ = int(l + (r-l)/2)
            
            if b_nums[mid_] > target:
                r = mid_ - 1
            elif b_nums[mid_] < target:
                l = mid_ + 1 
            elif b_nums[mid_] == target:
                best = mid_
                b_nums[best] = target + 1
                right = mid_ - 1
        l = 0
        r = len(nums) - 1       
        while l <= r:
            mid_ = int(l + (r-l)/2)
            
            if l_nums[mid_] > target:
                r = mid_ - 1
            elif l_nums[mid_] < target:
                l = mid_ + 1 
            elif l_nums[mid_] == target:
                last = mid_
                l_nums[last] = target - 1
                left = mid_ + 1

        ans = [best,last]
        return ans