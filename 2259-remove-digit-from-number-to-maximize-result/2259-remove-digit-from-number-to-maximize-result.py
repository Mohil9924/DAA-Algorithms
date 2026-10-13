class Solution(object):
    def removeDigit(self, number, digit):
        last_occurrence = -1
        
        for i in range(len(number)):
            if number[i] == digit:
                last_occurrence = i
                # Greedy choice: if removing this digit causes the next character to be strictly larger,
                # we immediately remove this digit to maximize the resulting number.
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i + 1:]
                    
        # If no such instance was found, remove the last occurrence of digit
        return number[:last_occurrence] + number[last_occurrence + 1:]