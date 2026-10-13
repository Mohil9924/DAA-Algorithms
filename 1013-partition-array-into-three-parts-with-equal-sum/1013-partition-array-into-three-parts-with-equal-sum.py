class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, we cannot divide it into 3 equal parts
        if total_sum % 3 != 0:
            return False
            
        target = total_sum // 3
        current_sum = 0
        parts_found = 0
        
        # Traverse up to len(arr) - 1 to ensure the 3rd part is non-empty
        for i in range(len(arr) - 1):
            current_sum += arr[i]
            
            if current_sum == target:
                parts_found += 1
                current_sum = 0
                
                # If we have found 2 parts with the target sum, 
                # the remaining non-empty slice must also sum to target
                if parts_found == 2:
                    return True
                    
        return False