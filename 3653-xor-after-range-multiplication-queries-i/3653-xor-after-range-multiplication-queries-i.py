import math
from functools import reduce

class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        limit = int(math.isqrt(n)) + 1
        
        # Stores total multiplier factors for small k values
        # small_k_mult[k][rem] will store difference array for range updates
        # where indices match `idx % k == rem`
        small_k = [{} for _ in range(limit)]
        
        for l, r, k, v in queries:
            if k >= limit:
                # Direct simulation for large k
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
            else:
                # Accumulate range multiplication for small k
                # Position of l and the first index beyond r with the same remainder mod k
                rem = l % k
                if rem not in small_k[k]:
                    small_k[k][rem] = [1] * (n // k + 2)
                
                start_step = l // k
                end_step = (r - rem) // k + 1
                
                diff = small_k[k][rem]
                diff[start_step] = (diff[start_step] * v) % MOD
                # Modular inverse to undo multiplication after end_step
                inv_v = pow(v, MOD - 2, MOD)
                diff[end_step] = (diff[end_step] * inv_v) % MOD

        # Apply accumulated small-k updates to nums
        for k in range(1, limit):
            for rem, diff in small_k[k].items():
                curr_mult = 1
                for step in range(len(diff) - 1):
                    curr_mult = (curr_mult * diff[step]) % MOD
                    idx = step * k + rem
                    if idx < n:
                        nums[idx] = (nums[idx] * curr_mult) % MOD

        # Compute bitwise XOR of all final elements
        return reduce(lambda x, y: x ^ y, nums)