def countingSort(arr):
    # Write your code here
    
    

    ans = [0 for x in range(100)] 
    
    
    for i in range(len(arr)):
        ans[arr[i]] += 1
        
        
        
    return(ans)