class Solution(object):
    def splitNum(self, num):
        # Extract digits and sort them in ascending order
        digits = sorted(list(str(num)))
        
        num1 = 0
        num2 = 0
        
        # Distribute digits alternately to num1 and num2
        for i in range(len(digits)):
            if i % 2 == 0:
                num1 = num1 * 10 + int(digits[i])
            else:
                num2 = num2 * 10 + int(digits[i])
                
        return num1 + num2