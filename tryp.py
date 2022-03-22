heights = [4,2,0,3,2,4,3,4]
max_ = min(heights) *len(heights)


for i in range(len(heights)):
    if (i - 1 >= 0 and heights[i] == heights[i-1]) or (i +1 < len(heights) and heights[i] ==  heights[i +1]):
            break
    width = 1
    j = i +1
    while j < len(heights):
        if heights[j] < heights[i]:
            break
        width += 1
        j += 1
    j = i -1
    while j > 0:
        if heights[j] < heights[i]:
            break
        width += 1
        j -= 1
    
    max_ = max(max_, width *heights[i])

print(max_)