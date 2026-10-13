class Solution(object):
    def buyChoco(self, prices, money):
        # Track the two smallest prices in a single pass
        min1 = float('inf')
        min2 = float('inf')
        
        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price
                
        total_cost = min1 + min2
        
        # Check if we can afford both chocolates without going into debt
        if total_cost <= money:
            return money - total_cost
        
        return money