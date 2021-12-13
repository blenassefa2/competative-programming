def insertionSort1(n, arr):
    # Write your code here
    last = arr[n-1]
    done = False
    #start from n-2 to 0
    counter = n-2
    while(counter >=-1):
        
        if arr[counter]>last:
            
            arr[counter+1] = arr[counter]
            if counter== -1:
                arr[counter+1] = last
        else:
            arr[counter+1] = last
            done =True
        for a in range(n):
            print (arr[a],end=" ")
        print()
        counter-=1
        if done:
            break
