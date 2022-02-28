class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_ = []
        sum_ = 0
        i = 0
        while i < len(heights)-1:
            if heights[i+1] <= heights[i]:
                i += 1
            else:
                b =heights[i+1] - heights[i]
                
                if len(min_) < ladders:
                    heappush(min_, b)
                    i+= 1
                    continue
                
                if min_ and min_[0] < b:
                    sum_ += heappop(min_)
                    heappush(min_,b)
    
                else:
                    sum_ += b
                
                if sum_ > bricks:
                    break
                i+= 1
        return i
                    