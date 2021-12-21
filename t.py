temperatures = [55,38,53,81,61,93,97,32,43,78]
   
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
        if not (bool(stack)):
            stack.append(i)
            i+=1
            continue
        if temperatures[stack[-1]] <temperatures[i]:
            
            
            continue
    
        stack.append(i)
        i+=1
    else:
        stack.append(i)
        i+=1
    
for i in stack:
    ans.append([i,0])
ans.sort()
c = len(stack)
t = [x[1] for x in ans]

print(t)