class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        temp = [0]*(max(nums)+1)
        stored = []
        result = 0
        li = []
        for i in range(len(nums)):
            temp[nums[i]] += 1
        for i in range(len(temp)):
            if temp[i] >= 1:
                s = i
                i+=temp[i]
                stored.extend([s]*temp[s])
                if s == target:
                    result = temp[s]

        if result >0:
            start = stored.index(target)
            for x in range(start, start+result):
                li.append(x)
        
        return li       
            