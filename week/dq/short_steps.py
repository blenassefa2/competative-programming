class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        [48,61,73,15,83,4,5,22,61,80,4,92,9,91,89,94,28,13,57,94,55,2,24,23,26,31,66,18,62,4,99,60,35,10,61]
                | |
         
        left =[(3,2),(5,1),(1,2)] = 2
        right = [(1,1),(2,1),(4,1),(3,1)] = 1
        
        9 - 3 = 6
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 0
            return 1
            
        
        right, left = defaultdict(int), defaultdict(int)
        
        l,r = 0,1
        
        while l < len(nums):
            if l < len(nums):
                left[nums[l]] += 1
                l += 2
            if r < len(nums):
                right[nums[r]] += 1
            
                r += 2
        
        max_l,max_r = [(i,left[i]) for i in left],[(j,right[j]) for j in right]
        max_l.sort(key = lambda x: (x[1],x[0]))
        max_r.sort(key = lambda x: (x[1],x[0]))
        sum_ = 0
        t = len(max_l)
        y = len(max_r)
        
        sum_1,sum_2 = max_l[-1][1],max_r[-1][1]
        if max_l[-1][0] == max_r[-1][0]:
            if y > 1:
                sum_1 += max_r[-2][1]
            if t > 1:
                sum_2 += max_l[-2][1]
            sum_ = max(sum_1,sum_2)
            
        else:
            sum_ = max_l[-1][1] + max_r[-1][1]
        
        
        return len(nums) - (sum_)
        
        