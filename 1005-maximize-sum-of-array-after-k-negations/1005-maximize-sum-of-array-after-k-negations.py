class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        # Sort the array in ascending order
        nums.sort()
        
        # Step 1: Flip negative numbers to positive (starting with the smallest negative)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
                
        # Step 2: If k is still odd, flip the smallest number in the modified array
        if k % 2 == 1:
            min_idx = nums.index(min(nums))
            nums[min_idx] = -nums[min_idx]
            
        return sum(nums)