class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lis = defaultdict(list)
        
        for i in range(len(s)):
            if len(lis[s[i]]) < 2:
                lis[s[i]].append(i)
            else:
                lis[s[i]][1] = i
        ans =[]
        for i in lis:
            if len(lis[i]) == 1:
                lis[i].append(lis[i][0])
            ans.append(lis[i])
        
        merged = [ans[0]]
        ans= ans[1:]
        for i in ans:
           
            if i[0] > merged[-1][1]:
                merged.append(i)
            elif i[0] <= merged[-1][1] and i[1] >= merged[-1][1]:
                a = [merged[-1][0],i[1]]
                merged.pop()
                merged.append(a)
        final = []
        for i in merged:
            final.append((i[1] - i[0])+1)
        
        return final