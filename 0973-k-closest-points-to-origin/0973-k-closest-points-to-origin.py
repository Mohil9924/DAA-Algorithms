import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            dist = x * x + y * y
            # Push -dist because Python's heapq is a min-heap by default
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        return [pt for _, pt in max_heap]