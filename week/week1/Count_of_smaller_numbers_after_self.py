class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = [0]*(max(nums)+1)
        stored = []
        result = []
        for i in range(len(nums)):
            temp[nums[i]] += 1

        for i in range(len(temp)):
            if temp[i] >= 1:
                s = i
                i+=temp[i]
                stored.extend([s]*temp[s])
                    

        for i in range(len(nums)):
            amount = stored.index(nums[i])
            result.append(amount)
        return result