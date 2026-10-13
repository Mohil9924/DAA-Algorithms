class Solution(object):
    def maximumOddBinaryNumber(self, s):
        # Count the number of '1's and '0's in the binary string
        ones = s.count('1')
        zeros = s.count('0')
        
        # To make the number odd, 1 '1' must be placed at the least significant bit (end).
        # To maximize the value, place the remaining (ones - 1) '1's at the most significant bits (start),
        # followed by all '0's, and finally the reserved '1' at the end.
        return '1' * (ones - 1) + '0' * zeros + '1'