class Solution:
    def countElements(self, nums: list[int], k: int) -> int:
        if k == 0:
            return len(nums)
        if k > len(nums):
            return 0
        
        # Sort in descending order
        nums.sort(reverse=True)
        
        # Threshold element: there are (k) elements >= nums[k - 1]
        threshold = nums[k - 1]
        
        # Count elements strictly smaller than threshold
        return sum(1 for x in nums if x < threshold)