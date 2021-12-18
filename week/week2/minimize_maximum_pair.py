class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nw = []
        l = len(nums) //2
        for i in range(l):
            nw.append([i, -1 *(i +1)])
        
        least_max = max([nums[x[0]] +nums[x[1]] for x in nw] )  
        return least_max 