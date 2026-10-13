class Solution(object):
    def minTimeToType(self, word):
        total_time = 0
        prev_char = 'a'
        
        for char in word:
            # Calculate absolute distance between current and target character
            diff = abs(ord(char) - ord(prev_char))
            
            # Shortest distance clockwise or counterclockwise
            move_time = min(diff, 26 - diff)
            
            # Add move time + 1 second to type the character
            total_time += move_time + 1
            
            # Update previous character pointer
            prev_char = char
            
        return total_time