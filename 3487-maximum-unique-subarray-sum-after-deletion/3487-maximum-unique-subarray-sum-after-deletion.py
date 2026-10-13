class Solution(object):
    def maxSum(self, nums):
        # Filter for positive elements and keep unique values
        positives = set()
        for x in nums:
            if x > 0:
                positives.add(x)
                
        # If there are positive numbers, the maximum sum is the sum of all unique positive numbers
        if positives:
            return sum(positives)
            
        # If all numbers are non-positive, return the maximum single element in nums
        return max(nums)