class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        # Step 1: Collect nodes in sorted order via in-order traversal
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        # Step 2: Build height-balanced BST using divide and conquer
        def build_balanced_bst(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            mid = (left + right) // 2
            curr = nodes[mid]

            curr.left = build_balanced_bst(left, mid - 1)
            curr.right = build_balanced_bst(mid + 1, right)

            return curr

        return build_balanced_bst(0, len(nodes) - 1)