class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lis = defaultdict(list)
        
        for i in range(len(s)):
            if len(lis[s[i]]) < 2:
                lis[s[i]].append(i)
            else:
                lis[s[i]][1] = i
        merged =[]
        for i in lis:
            merged.append(lis[i])
        for i in range(len(merged)):
            if len(merged[i]) == 1:
                merged[i].append(merged[i][0])
        merged.sort(key = lambda x:(x[0],x[1]))

        ans = [merged[0]]
        merged= merged[1:]
        for i in merged:
           
            if i[0] > ans[-1][1]:
                ans.append(i)
            elif i[0] <= ans[-1][1] and i[1] >= ans[-1][1]:
                a = [ans[-1][0],i[1]]
                ans.pop()
                ans.append(a)
        final = []
        for i in ans:
            final.append((i[1] - i[0])+1)
        
        return final