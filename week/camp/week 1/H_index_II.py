class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = max(citations)
        
        while start <= end:
            mid = int((start + end)/2)
            x = 0
            for i in range(len(citations)): 
                if citations[i] >= mid:
                    x+=1
            
            
            if x < mid: 
                end = mid - 1
            else:
                best = mid
                start = mid + 1
        return best