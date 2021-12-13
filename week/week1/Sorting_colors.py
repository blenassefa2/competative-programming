class Solution:
    def select(self, nums:List[int], i: int) -> int:
        minimum = nums[i]
        index = i
        for n in range(i,len(nums)):
            if minimum >nums[n]:
                minimum = nums[n]
                index = n
        return index
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            place = self.select(nums,i)
            nums[place], nums[i] = nums[i], nums[place]
        