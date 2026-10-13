class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        # Sort nums to easily access the largest and smallest elements
        nums.sort()
        
        # To maximize a + b - c, pick the two largest numbers for a and b,
        # and the single smallest number for c.
        c = nums[0]
        b = nums[-2]
        a = nums[-1]
        
        return a + b - c