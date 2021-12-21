class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        stack = []
        i = 0
        while i < (len(temperatures)):
            if not (bool(stack)):
                stack.append(i)
                i+=1
                continue
            last = stack[-1]

            if temperatures[last] <temperatures[i]:

                ans.append([last,i - last])
                stack.pop()
                if not (bool(stack)) or temperatures[stack[-1]] > temperatures[i]:
                    stack.append(i)
                    i+=1
                    continue
            else:
                stack.append(i)
                i+=1

        for i in stack:
            ans.append([i,0])
        ans.sort()
        t = [x[1] for x in ans]
        
        return t