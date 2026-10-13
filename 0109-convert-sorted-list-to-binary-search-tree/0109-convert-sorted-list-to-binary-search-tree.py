# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 1: Collect values into an array
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # Step 2: Build height-balanced BST recursively
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(vals[mid])

            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)

            return root

        return build_bst(0, len(vals) - 1)