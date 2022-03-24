class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum_ = 0
        for i in range(len(nums)):
            min_= nums[i]
            max_ = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] > max_:
                    max_ = nums[j]
                if nums[j] < min_:
                    min_ = nums[j]
                sum_ += (max_ - min_)
        return sum_