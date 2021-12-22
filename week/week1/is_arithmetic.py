class Solution:
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        Dict = []
        
        for i in range(len(l)):
            Dict.append((l[i], r[i]))
        ans = []
        
        for init,final in Dict:
            
            value = nums[init:final+1]  
            value.sort(reverse = True)
            t = value[0] - value[1]
            is_arithmetic = True
            
            for i in range(len(value)-1):
                if value[i] - value[i + 1] != t:
                    is_arithmetic = False
                    break
            ans.append(is_arithmetic)
        return ans