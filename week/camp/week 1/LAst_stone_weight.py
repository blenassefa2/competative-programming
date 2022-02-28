class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-1* x for x in stones]
        heapify(heap)
        
        
        while len(heap) != 1:
            a = -1 * heappop(heap)
            if not heap:
                return 0
            b = -1 * heappop(heap)
            if a != b:
                heappush(heap,-1 *( a - b))
            if not heap:
                return 0
        return -1 * heap[0]
        