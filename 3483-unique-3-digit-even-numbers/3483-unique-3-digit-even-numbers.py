class Solution(object):
    def totalNumbers(self, digits):
        # Count available digit frequencies
        freq = {}
        for d in digits:
            freq[d] = freq.get(d, 0) + 1
        
        count = 0
        
        # Check all possible 3-digit even numbers (100 to 998)
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Count required frequencies for the candidate number
            num_freq = {}
            for d in (d1, d2, d3):
                num_freq[d] = num_freq.get(d, 0) + 1
            
            # Check if available digits satisfy requirements
            valid = True
            for d, qty in num_freq.items():
                if freq.get(d, 0) < qty:
                    valid = False
                    break
            
            if valid:
                count += 1
                
        return count