class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)

        for i in words:
            counts[i] +=1
        c = (sorted(counts.items(), key = lambda x: (-1*x[1],x[0])))
        
        
        ans = []

        for i in range(k):
            ans.append(c[i][0])

        
        return ans