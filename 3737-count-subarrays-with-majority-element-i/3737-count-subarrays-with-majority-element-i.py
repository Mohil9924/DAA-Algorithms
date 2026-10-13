class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Offset to handle negative prefix sums (min prefix sum can be -n)
        OFFSET = n
        
        # Frequency array for prefix sums
        freq = [0] * (2 * n + 1)
        freq[0 + OFFSET] = 1  # Initial prefix sum P[0] = 0
        
        prefix_sum = 0
        ans = 0
        
        # Maintains the total count of prefix sums strictly smaller than current prefix_sum
        smaller_count = 0 
        
        for num in nums:
            val = 1 if num == target else -1
            
            if val == 1:
                # When moving from prefix_sum to prefix_sum + 1,
                # all previous occurrences of `prefix_sum` now become strictly smaller.
                smaller_count += freq[prefix_sum + OFFSET]
                prefix_sum += 1
            else:
                # When moving from prefix_sum to prefix_sum - 1,
                # all previous occurrences of `prefix_sum - 1` are no longer strictly smaller.
                prefix_sum -= 1
                smaller_count -= freq[prefix_sum + OFFSET]
                
            ans += smaller_count
            freq[prefix_sum + OFFSET] += 1
            
        return ans