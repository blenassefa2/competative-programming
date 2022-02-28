k = 3
i = 0
nums = [1,1,2,1,1]
k = 3
lst = []
final = 0

while i < len(nums):
    
    
        count = k 
        j = i
        while j < len(nums) and count >= 0:
            if nums[j] % 2 != 0:
                count -= 1 
            j += 1
        final += 1

        while i < j:
            if nums[i] % 2 != 0:
                break
            final += 1
            i+= 1
        
    
print(final)