class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        outpt, dq, once, twc = [], deque([]), set(), set()
        
        for i in range(len(s)+ 1):
            if len(dq) < 10:
                dq.append(s[i])
                continue
            tmp = "".join(dq)
            if tmp in once and tmp not in twc:
                outpt.append(tmp)
                twc.add(tmp)
            once.add(tmp)
            if i >= len(s):
                break
            dq.popleft()
            dq.append(s[i])
        return outpt
                