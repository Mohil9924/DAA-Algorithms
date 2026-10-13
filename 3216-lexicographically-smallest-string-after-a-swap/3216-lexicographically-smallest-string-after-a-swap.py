class Solution(object):
    def getSmallestString(self, s):
        chars = list(s)
        
        # Look for the first adjacent pair with same parity where left > right
        for i in range(len(chars) - 1):
            d1 = int(chars[i])
            d2 = int(chars[i + 1])
            
            # Check if both digits have the same parity
            if d1 % 2 == d2 % 2:
                # Swapping smaller digit to the left creates a smaller string
                if d1 > d2:
                    chars[i], chars[i + 1] = chars[i + 1], chars[i]
                    break
                    
        return "".join(chars)