h1 = [48,99,37,4,-31]

k = 140
sum_ = 0
found = False
zeros = 0
sub = sum(h1)
min_ = len(h1)
for x in range(len(h1)):
    i = x+2
    t = h1[x:i]
    print(t)
    if sum(t) >= k:
        print(t)
        found = True
        if min_ > len(t):
            min_ = len(t) 

if found:
    print(min_) 
else:
    print(-1)

