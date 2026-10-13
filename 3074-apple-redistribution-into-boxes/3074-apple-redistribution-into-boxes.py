class Solution(object):
    def minimumBoxes(self, apple, capacity):
        # Calculate total number of apples to store
        total_apples = sum(apple)
        
        # Sort box capacities in descending order to use largest boxes first
        capacity.sort(reverse=True)
        
        boxes_used = 0
        current_capacity = 0
        
        # Greedily pick the box with the maximum capacity remaining
        for cap in capacity:
            current_capacity += cap
            boxes_used += 1
            if current_capacity >= total_apples:
                return boxes_used
                
        return boxes_used