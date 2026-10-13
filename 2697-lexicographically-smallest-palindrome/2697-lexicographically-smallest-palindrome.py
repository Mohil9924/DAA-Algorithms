class Solution(object):
    def makeSmallestPalindrome(self, s):
        chars = list(s)
        left = 0
        right = len(chars) - 1
        
        while left < right:
            if chars[left] != chars[right]:
                # Greedily replace the larger character with the smaller character
                smaller_char = min(chars[left], chars[right])
                chars[left] = smaller_char
                chars[right] = smaller_char
            left += 1
            right -= 1
            
        return "".join(chars)