class Solution(object):
    def minMaxDifference(self, num):
        s = str(num)
        
        # To find the maximum value, replace the first digit that is not '9' with '9'
        max_str = s
        for ch in s:
            if ch != '9':
                max_str = s.replace(ch, '9')
                break
                
        # To find the minimum value, replace the first digit (s[0]) with '0'
        # Since leading zeros are allowed, converting the first digit to '0' yields the smallest possible value
        min_str = s.replace(s[0], '0')
        
        return int(max_str) - int(min_str)