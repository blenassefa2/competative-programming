class MedianFinder:

    def __init__(self):
        self.min_ = []
        self.max_ = []
        self.median = -10000000
        self.final= []

    def addNum(self, num: int) -> None:
        if self.median < num:
            heappush(self.min_,num)
        else:
            heappush(self.max_, -1 * num)
            
        if len(self.min_) == len(self.max_):
            self.final.append(float(((-1 * self.max_[0]) + self.min_[0])/2))
            # median = ((-1 * max_[0]) + min_[0])/ 2
            self.median = self.final[-1]
            
        elif len(self.min_) == len(self.max_) + 1:
            self.final.append(float(self.min_[0]))
            self.median = self.final[-1]
            
        elif len(self.min_) + 1 == len(self.max_):
            self.final.append(float((-1 * self.max_[0])))
            self.median = self.final[-1]
            
        elif len(self.min_) > len(self.max_)+1:
            heappush(self.max_,(-1 * heappop(self.min_)))
            self.final.append(float(((-1 * self.max_[0]) + self.min_[0])/2))
            self.median = self.final[-1]
                           
        elif len(self.min_) + 1 < len(self.max_):
            heappush(self.min_,(-1*heappop(self.max_)))
            self.final.append(float(((-1 * self.max_[0]) + self.min_[0])/2))
            self.median = self.final[-1]
        

    def findMedian(self) -> float:
        return self.final[-1]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()