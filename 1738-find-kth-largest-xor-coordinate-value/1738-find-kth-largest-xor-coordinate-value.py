import heapq

class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor_sum = [[0] * n for _ in range(m)]
        
        # Min-Heap to maintain the k largest values
        min_heap = []

        for r in range(m):
            for c in range(n):
                top = xor_sum[r - 1][c] if r > 0 else 0
                left = xor_sum[r][c - 1] if c > 0 else 0
                top_left = xor_sum[r - 1][c - 1] if r > 0 and c > 0 else 0
                
                # Dynamic programming state transition
                xor_sum[r][c] = matrix[r][c] ^ top ^ left ^ top_left
                
                # Maintain top k values in min_heap
                heapq.heappush(min_heap, xor_sum[r][c])
                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        return min_heap[0]