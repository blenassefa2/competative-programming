
class Solution:
    def calc(self,a,b, o):
        if o == "/":
            return(a//b)
        if o == "*":
            return(a*b)
        if o == "+":
            return(a+b)
        return(a-b)
    def calculate(self, s: str) -> int:
        s = "".join(s.split(" "))
        operand = {"/":1, "*":1,"-":0, "+":0}
        op = []
        n = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = s[i]
                t = i
                while t+1 < len(s) and s[t+1] not in operand:
                    t +=1
                    num = num + s[t]
                i = t
                n.append(num)
            else:
                if op == []:
                    op.append(s[i])
                
                elif operand[op[-1]] >=operand[s[i]]:
                    a,b = int(n[-2]),int(n[-1])
                    n.pop()
                    n.pop()
                    n.append(self.calc(a,b,op[-1]))
                    op.pop()
                    
                    continue
                else:
                    op.append(s[i])
            i +=1
        while op != []:
            a,b = int(n[-2]),int(n[-1])
            n.pop()
            n.pop()
            n.append(self.calc(a,b,op[-1]))
            op.pop()
        result = n[0]
        
        return result
                