class Solution(object):
    def distMoney(self, money, children):
        # Every child must receive at least 1 dollar
        if money < children:
            return -1
            
        # Give 1 dollar to each child first
        money -= children
        
        # Calculate how many children can receive 7 additional dollars (totaling 8 dollars)
        ans = money // 7
        rem = money % 7
        
        # Case 1: More than 'children' count can get 8 dollars, or exact match with remaining money left over
        if ans > children or (ans == children and rem > 0):
            return children - 1
            
        # Case 2: One child is left with 3 additional dollars (1 + 3 = 4 dollars), which is forbidden
        if ans == children - 1 and rem == 3:
            return ans - 1
            
        return ans