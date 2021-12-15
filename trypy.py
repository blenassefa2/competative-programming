arr = [1,2,3,1,1,3]

def factorial (n):
    if n <= 1:
        return 1
    else:
        return n*(factorial(n-1))

repititions = [arr.count(i) for i in arr]

x = 1
for i in repititions:
    x +=i
print(x)