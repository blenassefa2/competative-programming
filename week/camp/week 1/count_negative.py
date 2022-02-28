class Solution:
    def binary_search(self,l):
        best = len(l)
        right = len(l)
        left = 0
        while left <= right:
            median = int(left + (right - left)/ 2)
            if l[median] >= 0:
                left = median + 1
            else:
                if best > median:
                    best = median
                right = median - 1
        return best
    def countNegatives(self, grid: List[List[int]]) -> int:
        sum_= 0
        for i in grid:
            if i[-1] < 0:
                first = self.binary_search(i)
                sum_ += (len(i) - first)
        return sum_