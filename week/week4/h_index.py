class Solution:
    def hIndex(self, citations: List[int]) -> int:
        t = max(citations)
        hindices =[]
        for i in range(t+1):
            nw = [x for x in citations if x>=i]
            
            if len(nw) >= i:
                hindices.append(i)
            
        hindices.append(0)
            
        return max(hindices)