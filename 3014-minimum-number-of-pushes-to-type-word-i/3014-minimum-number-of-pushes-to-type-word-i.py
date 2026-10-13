class Solution(object):
    def minimumPushes(self, word):
        # Since all characters in word are distinct, n is the number of letters.
        n = len(word)
        pushes = 0
        
        # There are 8 available keys (2 to 9).
        # First 8 letters require 1 push each.
        # Next 8 letters require 2 pushes each.
        # Next 8 letters require 3 pushes each.
        # Remaining letters require 4 pushes each.
        for i in range(n):
            pushes += (i // 8) + 1
            
        return pushes