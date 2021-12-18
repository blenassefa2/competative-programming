def countingValleys(steps, path):
   
    
    arr = []
    for letter in path:
        
        if letter == "U":
            arr.append(1)
        elif letter == "D":
            arr.append(-1)
    t = 0 
    count = 0

    for a in range(len(arr)):
        t += arr[a]
        if t == 0 and arr[a] == 1:
            count+=1
    return(count)