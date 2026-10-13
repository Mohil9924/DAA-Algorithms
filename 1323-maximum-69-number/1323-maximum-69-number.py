class Solution(object):
    def maximum69Number(self, num):
        # Convert integer to string to replace the first '6' with '9'
        num_str = str(num)
        
        # Replace only the first occurrence of '6' with '9'
        max_str = num_str.replace('6', '9', 1)
        
        return int(max_str)