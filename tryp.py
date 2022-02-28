import sys
import heapq
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))



def calc_(sum_, max_,limit,i,cp):
    if sum_ >= limit:
        return((i+cp))
    
    return min(calc_(sum_+ 1,max_+1,limit,i +1,cp),calc_(sum_ + max_,max_,limit,i,cp+1))
    
    
    

    
w = inp()
counter = 0   
print(calc_(1,1,w,0,0))