class Solution(object):
    def minimumSum(self, num):
        # Extract digits and sort them in ascending order
        digits = sorted(list(str(num)))
        
        # Form the two smallest 2-digit numbers
        # Tens digits get the two smallest values: digits[0] and digits[1]
        # Ones digits get the two largest values: digits[2] and digits[3]
        new1 = int(digits[0] + digits[2])
        new2 = int(digits[1] + digits[3])
        
        return new1 + new2