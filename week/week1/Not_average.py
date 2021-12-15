class Solution:
    def is_correct(self,arr):
        done = True
        b = len(arr)
        i = 1
        while i< b -1: 
            if(arr[i-1] + arr[i+1])/2 == arr[i]:
                done = False
                break
            i += 1
    
        return done
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = nums
        while not self.is_correct(nums):
            i = 1
    
            while i < len(a) -1:
                if(a[i-1] + a[i+1])/2 == a[i]:
                    a[i-1], a[i] = a[i], a[i-1]
            
                i+= 1
        return a