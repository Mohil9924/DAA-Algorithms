from collections import Counter

class Solution(object):
    def minDeletion(self, s, k):
        # Count frequency of each character in s
        counts = Counter(s)
        
        # If the number of distinct characters is already <= k, no deletions needed
        if len(counts) <= k:
            return 0
            
        # Sort frequencies in ascending order
        freqs = sorted(counts.values())
        
        # To minimize deletions, delete characters with the smallest frequencies
        # We need to remove (len(counts) - k) distinct character types completely
        num_to_remove = len(counts) - k
        
        return sum(freqs[:num_to_remove])