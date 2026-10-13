class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # The root of the left child is the second element in preorder
        left_root_val = preorder[1]
        
        # Find the index of left child's root in postorder array
        # This tells us the size of the left subtree
        left_subtree_size = postorder.index(left_root_val) + 1
        
        # Recursively construct left and right subtrees
        root.left = self.constructFromPrePost(
            preorder[1 : 1 + left_subtree_size], 
            postorder[:left_subtree_size]
        )
        root.right = self.constructFromPrePost(
            preorder[1 + left_subtree_size :], 
            postorder[left_subtree_size:-1]
        )
        
        return root