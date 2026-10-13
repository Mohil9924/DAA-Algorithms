class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        res = [1]
        
        while len(res) < n:
            # Generate odd transformation and even transformation
            odds = [2 * x - 1 for x in res if 2 * x - 1 <= n]
            evens = [2 * x for x in res if 2 * x <= n]
            
            # Combine odds on left, evens on right
            res = odds + evens
            
        return res