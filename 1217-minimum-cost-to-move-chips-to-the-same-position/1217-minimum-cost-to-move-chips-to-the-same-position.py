class Solution(object):
    def minCostToMoveChips(self, position):
        even_count = 0
        odd_count = 0
        
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
        # Move the smaller group of chips to the larger group's parity position
        return min(even_count, odd_count)