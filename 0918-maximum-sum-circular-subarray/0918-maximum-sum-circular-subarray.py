class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        
        max_sum = nums[0]
        cur_max = 0
        
        min_sum = nums[0]
        cur_min = 0
        
        for num in nums:
            total_sum += num
            
            # Standard Kadane's for Maximum Subarray Sum
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            
            # Standard Kadane's for Minimum Subarray Sum
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
        
        # Edge Case: If all elements are negative, max_sum is the largest single element
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)