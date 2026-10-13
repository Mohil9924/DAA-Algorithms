class Solution(object):
    def largestPerimeter(self, nums):
        # Sort the array in ascending order
        nums.sort()
        
        # Iterate backwards to find the largest valid triangle
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
                
        return 0