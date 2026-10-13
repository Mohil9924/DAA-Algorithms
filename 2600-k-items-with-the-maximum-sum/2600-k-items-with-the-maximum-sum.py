class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        # Greedily take as many 1s as possible
        if k <= numOnes:
            return k
        
        # Take all 1s and as many 0s as possible (0s do not change the sum)
        if k <= numOnes + numZeros:
            return numOnes
            
        # Take all 1s, all 0s, and the remaining count as -1s
        return numOnes - (k - numOnes - numZeros)