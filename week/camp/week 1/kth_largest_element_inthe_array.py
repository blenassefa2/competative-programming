class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*x for x in nums]
        heapify(nums)
        t = 0
        for i in range(k):
            t = -1* heappop(nums)
        return t
            