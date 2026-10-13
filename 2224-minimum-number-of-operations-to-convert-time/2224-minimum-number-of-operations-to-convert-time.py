class Solution(object):
    def convertTime(self, current, correct):
        # Convert HH:MM time strings to total minutes from midnight
        cur_mins = int(current[:2]) * 60 + int(current[3:])
        cor_mins = int(correct[:2]) * 60 + int(correct[3:])
        
        diff = cor_mins - cur_mins
        ops = 0
        
        # Greedily subtract the largest possible increments (60, 15, 5, 1)
        for increment in [60, 15, 5, 1]:
            ops += diff // increment
            diff %= increment
            
        return ops