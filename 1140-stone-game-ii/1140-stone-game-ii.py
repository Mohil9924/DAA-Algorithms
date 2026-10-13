from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            # If current player can take all remaining piles
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                # Opponent gets dp(i + X, max(M, X)), leaving the rest for current player
                current_player_stones = suffix_sum[i] - dp(i + X, max(M, X))
                max_stones = max(max_stones, current_player_stones)
                
            return max_stones

        return dp(0, 1)