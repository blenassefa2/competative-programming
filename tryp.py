arr = [1,3,4,2,6,8]


odds = [x for x in arr if x%2 != 0]
evens = [x for x in arr if x%2 == 0]
is_changed = True

if len(arr) ==0 or len(odds) > len(evens) or len(arr) %2 != 0:
    is_changed = False

if not is_changed:
    print ([])
    exit()


for y in evens:
   
    if y/2 in evens:
        evens.remove(y/2)
        odds.append(y/2)

original = []

for y in evens:
    if y/2 in odds:
        original.append(int(y/2))
    elif y/2 in evens:
        original.append(int(y))



    
print(original)
