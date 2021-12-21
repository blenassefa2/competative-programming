from collections import defaultdict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        k = len(arr) // 2
        
        counts = defaultdict(int)

        for i in arr:
            counts[i] +=1
        c = (sorted(counts.values(), reverse = True))
        
        

        val = 0
        size = 0
        for i in c:
            size +=i
            val += 1
            if k<=size:
                break

        return val