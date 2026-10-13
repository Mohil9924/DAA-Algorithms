import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        count = Counter(nums)
        
        # Step 2 & 3: Keep a min-heap of size k
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # Step 4: Extract elements from the heap
        return [num for freq, num in min_heap]