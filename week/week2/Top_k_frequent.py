from collections import defaultdict
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for i in nums:
            counts[i] +=1
        c = (sorted(counts.items(), reverse = True, key = lambda x:x[1]))

        ans = []

        for i in range(k):
            ans.append(c[i][0])

        
        return ans