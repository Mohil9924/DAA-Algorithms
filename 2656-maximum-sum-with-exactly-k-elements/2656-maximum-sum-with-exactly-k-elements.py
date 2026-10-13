class Solution(object):
    def maximizeSum(self, nums, k):
        # Find the maximum element in nums
        max_num = max(nums)
        
        # We select max_num k times, incrementing it by 1 after each selection.
        # Total score = max_num + (max_num + 1) + ... + (max_num + k - 1)
        # Using arithmetic progression formula: k * max_num + k * (k - 1) // 2
        return k * max_num + (k * (k - 1)) // 2