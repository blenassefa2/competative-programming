class Solution:
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 0

        max_ = max(nums)
        nums.sort()
        best = max_
        lst = [i for i in range(1,max_ + 1)]
        r = len(lst) -1
        while l <= r:
            mid = int(l + (r-l)/2)
            sum_ = sum([ceil(i/lst[mid]) for i in nums ])
            if sum_ > threshold:
                l = mid + 1
            else:
                best = mid
                r = mid -1
        return lst[best]