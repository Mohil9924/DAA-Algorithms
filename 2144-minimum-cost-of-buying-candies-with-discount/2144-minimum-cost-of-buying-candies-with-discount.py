class Solution(object):
    def minimumCost(self, cost):
        # Sort costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        
        for i in range(len(cost)):
            # Every 3rd candy (at index 2, 5, 8, ...) is received for free
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost