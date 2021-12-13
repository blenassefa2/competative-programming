class Solution:
    def final_sort(self,t):
        l = len(t)
        f = [str(x) for x in t]
    
        for i in range(0,l-1,1):
            a = f[i] +f[i+1]
            b=f[i+1]+f[i]
            if a < b:
                t[i] ,t[i+1] = t[i+1],t[i]
    def better_sort(self,nw, max_dig):
        l = len(nw)
        a = [x for x in nw]
        dic = []
        for i in range(l):
        
            c = a[i]
            while len(str(a[i]))< max_dig:
                a[i] = (a[i]*(10)) + a[i]%10
        
            dic.append((c,a[i]))
    
        v = sorted(dic, key=lambda tup: (tup[1]),reverse = True)
    
    
    
        g = [v[a][0] for a in range(len(dic))]
    
        self.final_sort(g)
    
        return(g)
    def largestNumber(self, nums: List[int]) -> str:
        max_dig = len(str(max(nums)))

        stored = self.better_sort(nums,max_dig)
        
        li = ''.join([str(s) for s in stored])
        if stored[0] == 0:
            li = "0"
        return li