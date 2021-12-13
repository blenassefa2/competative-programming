intervals = [[1,4],[5,6]]
arr = []
if (len(intervals) == 1):
    arr = intervals


for i in range(len(intervals)-1):
    print(intervals[i][1] -intervals[i+1][0])
    if(intervals[i][1] -intervals[i+1][0] >=0):
        max_ = max([intervals[i][0], intervals[i][1],intervals[i+1][0],intervals[i+1][1]])
        min_ = min([intervals[i][0], intervals[i][1],intervals[i+1][0],intervals[i+1][1]])
        arr.append([min_,max_])
    else:
        if(i == 0):
            arr.append(intervals[i])
            arr.append(intervals[i+1])
        else:
            arr.append(intervals[i+1])
        
print(arr)

    
    



    




