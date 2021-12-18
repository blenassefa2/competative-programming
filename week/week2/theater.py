n, m,a, = list(map(int, input().split()))

width = int(n/a)if (n%a) == 0 else int(n/a)+1
height = int(m/a) if (m%a) == 0 else int(m/a) +1

total = width *height

print(total)