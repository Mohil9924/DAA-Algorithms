class Solution(object):
    def getLongestSubsequence(self, words, groups):
        result = []
        last_group = -1
        
        # Greedily pick words whenever the group changes
        for i in range(len(words)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]
                
        return result