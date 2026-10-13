class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        # Hash map to locate the root index in inorder traversal in O(1) time
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # The last element in postorder is the current root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Get the index of current root in inorder traversal
            inorder_idx = inorder_map[root_val]

            # Build right subtree first, then left subtree
            root.right = helper(inorder_idx + 1, right)
            root.left = helper(left, inorder_idx - 1)

            return root

        return helper(0, len(inorder) - 1)