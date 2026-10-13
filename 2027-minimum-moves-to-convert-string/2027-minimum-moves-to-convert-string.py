class Solution(object):
    def minimumMoves(self, s):
        moves = 0
        i = 0
        n = len(s)
        
        while i < n:
            # If we encounter an 'X', we must flip a 3-character block starting here
            if s[i] == 'X':
                moves += 1
                i += 3  # Skip the next 3 characters covered by this move
            else:
                i += 1  # Move to the next character if it's already 'O'
                
        return moves