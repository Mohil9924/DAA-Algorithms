class Solution(object):
    def diStringMatch(self, s):
        low = 0
        high = len(s)
        perm = []

        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # char == 'D'
                perm.append(high)
                high -= 1

        # Append the remaining last element
        perm.append(low)  # or perm.append(high), since low == high here

        return perm