class Solution(object):
    def minimumOperations(self, nums):
        # The minimum operations needed to make all elements 0 equals 
        # the number of unique strictly positive integers in nums.
        unique_positives = set()
        
        for num in nums:
            if num > 0:
                unique_positives.add(num)
                
        return len(unique_positives)