class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Create a sorted copy
        sorted_nums = sorted(nums)
        n = len(nums)
        
        # Step 2: Split indices into two halves (filling backwards to avoid duplicates overlap)
        mid = (n + 1) // 2
        small = sorted_nums[:mid]
        large = sorted_nums[mid:]
        
        # Step 3: Interleave into nums
        nums[::2] = small[::-1]  # Even indices get smaller half, reversed
        nums[1::2] = large[::-1]  # Odd indices get larger half, reversed