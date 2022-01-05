class Solution:
    def play(self,start , end , nums):
        if start == end:
            return nums[start]
        return max(nums[start] - self.play(start + 1, end,nums),nums[end]-self.play(start,end-1,nums))
    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = self.play(0 ,len(nums)-1,nums)
        if result < 0:
            return False
        else:
            return True