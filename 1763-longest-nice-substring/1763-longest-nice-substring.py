class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        char_set = set(s)
        
        for i, char in enumerate(s):
            # If the character's counterpart is missing, s cannot be nice across index i
            if char.swapcase() not in char_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                
                # Return the strictly longer substring; if equal, return 'left' for earliest occurrence
                return left if len(left) >= len(right) else right
        
        # All characters in s have both upper and lowercase versions
        return s