def trips(time, t, max_ ):
    sum_ = 0
    for i in time:
        if i <=t:
            sum_ += (t//i)
    if sum_ >=max_:
        return True
    return False
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = max(time) *totalTrips
        best = right
        while left<= right:
            mid = int(left + (right -left)/2)
            
            if not trips(time,mid, totalTrips):
                left = mid +1
            else:
                best = mid
                right = mid - 1
        return best
            