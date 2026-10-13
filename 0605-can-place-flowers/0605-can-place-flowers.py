class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            # Check if current plot is empty
            if flowerbed[i] == 0:
                # Check left and right neighbors (or array boundaries)
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                # If both neighbors are empty, we can plant a flower here
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    
                    # Early exit if required number of flowers are planted
                    if count >= n:
                        return True
                        
        return count >= n