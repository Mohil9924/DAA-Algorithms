import heapq

class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        # Min-heap ordered by (length, numeric string value)
        min_heap = []
        
        for num in nums:
            # Pushing (len(num), num) leverages tuple comparison:
            # 1. Compares length first
            # 2. Compares string lexicographically if lengths match
            heapq.heappush(min_heap, (len(num), num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        return min_heap[0][1]