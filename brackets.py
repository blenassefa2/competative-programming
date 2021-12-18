nums =[1,2,3,4]

k = 5

def not_done(arr,k):
    
    for a in arr:
        if k - a in arr:
            return True
            
    return False
nw = []
length = len(nums)

zeros = nums.count(0)    
for i in nums:
    t = k - i
    if t in nums:
        nums[i] = 0
    print(nums) 
        


length =nums.count(0) - zeros

print(int(length/2))