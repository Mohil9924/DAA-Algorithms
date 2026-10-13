class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        max_dist = 0
        
        # Check maximum distance starting from the leftmost house (index 0)
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
                
        # Check maximum distance starting from the rightmost house (index n - 1)
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist