class Solution(object):
    def largestInteger(self, n, s):
        # Maximum digit sum possible with at most n digits (all 9s)
        if s > 9 * n:
            return -1
            
        # Greedily place the maximum possible digit (up to 9) from left to right
        val = 0
        for _ in range(n):
            digit = min(9, s)
            val = val * 10 + digit
            s -= digit
            
        return val