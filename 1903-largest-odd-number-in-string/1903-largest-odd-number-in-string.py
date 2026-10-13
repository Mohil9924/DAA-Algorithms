class Solution(object):
    def largestOddNumber(self, num):
        # Scan from right to left to find the rightmost odd digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                # Return the prefix up to and including this odd digit
                return num[:i + 1]
                
        return ""