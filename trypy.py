s = "3[a2[c]]"
stack = ""
re = ""
for i in s:
    
    if i != "]":
        stack+=i
    else:
        r =""
        
        while stack[-1] != "[":
            r = stack[-1] + r
            stack = stack[:-1]
        r = r*int(stack[-2])
        stack = stack[:-2]
        stack += r
        re =r
print(re)