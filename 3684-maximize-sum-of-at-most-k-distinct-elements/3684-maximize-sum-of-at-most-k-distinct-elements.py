class Solution(object):
    def maxKDistinct(self, nums, k):
        # Extract unique values to satisfy the distinct numbers constraint
        unique_nums = sorted(list(set(nums)), reverse=True)
        
        # Select up to k largest distinct values
        return unique_nums[:k]