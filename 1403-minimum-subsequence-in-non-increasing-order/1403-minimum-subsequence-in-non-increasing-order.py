class Solution(object):
    def minSubsequence(self, nums):
        # Sort array in non-increasing order (descending)
        nums.sort(reverse=True)
        
        total_sum = sum(nums)
        subseq_sum = 0
        res = []
        
        for num in nums:
            subseq_sum += num
            res.append(num)
            # Check if subsequence sum is strictly greater than remaining sum
            if subseq_sum > total_sum - subseq_sum:
                break
                
        return res