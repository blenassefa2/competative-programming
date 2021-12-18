class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        a = len(piles) //3 
        l = len(piles)
        
        piles = sorted(piles)[a:l]
        
        my_total = 0

        for i in range(0,l - a,2):
            my_total +=piles[i]
            
            
        
        
        return my_total 
        