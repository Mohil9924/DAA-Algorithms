from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        # Count frequency of each character
        char_counts = Counter(s)
        
        length = 0
        has_odd = False
        
        for count in char_counts.values():
            # Add the largest even portion of the count
            length += (count // 2) * 2
            
            # Check if there is an odd count remaining
            if count % 2 == 1:
                has_odd = True
                
        # If any character had an odd count, we can place 1 odd character in the center
        if has_odd:
            length += 1
            
        return length