class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0],x[1] ))
       
        stack = [intervals[0]]
        intervals = intervals[1:]
        for i in intervals:
           
            if i[0] > stack[-1][1]:
                stack.append(i)
            elif i[0] <= stack[-1][1] and i[1] >= stack[-1][1]:
                a = [stack[-1][0],i[1]]
                stack.pop()
                stack.append(a)
            
        
        return stack