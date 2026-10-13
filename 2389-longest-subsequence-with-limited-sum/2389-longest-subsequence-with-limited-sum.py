import bisect

class Solution(object):
    def answerQueries(self, nums, queries):
        # Sort nums in ascending order to maximize subsequence size
        nums.sort()
        
        # Build prefix sums in-place
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        answer = []
        for q in queries:
            # bisect_right finds the count of elements in prefix sums <= q
            idx = bisect.bisect_right(nums, q)
            answer.append(idx)
            
        return answer