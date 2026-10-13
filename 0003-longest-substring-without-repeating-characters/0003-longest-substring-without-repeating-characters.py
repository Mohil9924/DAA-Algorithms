class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If the character is inside the current sliding window, move left pointer
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update last seen index of character
            char_map[char] = right
            
            # Calculate window length
            max_len = max(max_len, right - left + 1)
            
        return max_len