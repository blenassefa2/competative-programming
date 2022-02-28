class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        li = []
        for i  in range(len(matrix)):
            for j in range(len(matrix[i])):
                li.append(matrix[i][j])
                
        for i in li:
            heapq.heappush(heap, i)
        k= k -1    
        while k > 0:
            heapq.heappop(heap)
            k -= 1

        ans = heapq.heappop(heap)
        return ans