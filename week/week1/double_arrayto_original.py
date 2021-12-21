class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        arr = changed

        original = []
        arr.sort()
        
        Dict = defaultdict(deque)
        for i in range(len(arr)):
            Dict[arr[i]].append(i)
        
        visited =set()
        zeros = arr.count(0)
        
        if zeros%2 != 0:
            return original
        else:
            original = [0]*(zeros//2)
        
        
        i = zeros
        while i <len(arr):
        
            t = arr[i]
            
            if i not in visited:
                if t*2 not in Dict.keys():
                    break
                if len(Dict[t*2])!= 0:
                    visited.add(Dict[t*2][0])
                    visited.add(i)
                    Dict[t*2].popleft()
                    original.append(t)
                    
            i+= 1
        
        if len(visited) + zeros != len(arr):
            original = []
        
        return original


