class Solution(object):
    def minOperations(self, nums):
        operations = 0
        
        for i in range(1, len(nums)):
            # If current element is not strictly greater than previous element
            if nums[i] <= nums[i - 1]:
                # Target value needed to make it strictly increasing
                needed = nums[i - 1] + 1
                # Add the required operations
                operations += needed - nums[i]
                # Update current element to the newly incremented value
                nums[i] = needed
                
        return operations