from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        # Step 1: Count frequency of each character in the string
        count = Counter(s)
        
        # Step 2: Search for a character that breaks the condition (< k)
        for char, freq in count.items():
            if freq < k:
                # Step 3 & 4: Split string by this character and recursively call on segments
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # Base case: All characters meet the threshold k
        return len(s)