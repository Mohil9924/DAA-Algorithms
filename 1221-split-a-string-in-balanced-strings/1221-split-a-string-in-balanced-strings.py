class Solution(object):
    def balancedStringSplit(self, s):
        balance = 0
        count = 0
        
        for char in s:
            if char == 'L':
                balance += 1
            else:  # char == 'R'
                balance -= 1
                
            # Whenever balance reaches 0, a balanced substring is formed
            if balance == 0:
                count += 1
                
        return count