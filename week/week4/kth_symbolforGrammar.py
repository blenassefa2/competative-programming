class Solution:
    def recur(self, k, n,i):
        if n == 0:
            return i
        h = pow(2,n-1)
        if k > h:
            i += 1
            return self.recur(k-h,n-1,i)
        return self.recur(k,n-1,i)
    def kthGrammar(self, n: int, k: int) -> int:
        
        ans = self.recur(k,n-1,0)
        if ans %2 == 0:
            return "0"
        
        return "1"