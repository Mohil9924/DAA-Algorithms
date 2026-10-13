class Solution(object):
    def fillCups(self, amount):
        # Sort array to easily access maximum and total elements
        amount.sort()
        
        # Total sum of cups needed
        total_cups = sum(amount)
        max_cups = amount[2]
        
        # If one type is greater than the sum of the other two,
        # it bottlenecking us and will take max_cups seconds.
        # Otherwise, we can pair almost all cups together, taking ceil(total_cups / 2) seconds.
        return max(max_cups, (total_cups + 1) // 2)