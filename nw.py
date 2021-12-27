from typing import Deque


nums = [3,1,2,4,0,1]
k = 10


found = False
min_ = len(nums)
# for i in nums:
#     print([i])
for i in range(len(nums) -1):
    print([nums[i+x] for x in range(len(nums))])
# for i in range(len(nums) -2):
#     print([nums[i], nums[i+1], nums[i+2]])
# for i in range(len(nums) -3):
#     print([nums[i], nums[i+1], nums[i+2], nums[i+3]])

# for x in range(len(nums)):
#     for i in range(x +1,len(nums)+1):
#         t = nums[x:i]
#         print(t)
#         if sum(t) >= k:
#             found = True
#             if min_ > len(t):
#                 min_ = len(t) 



