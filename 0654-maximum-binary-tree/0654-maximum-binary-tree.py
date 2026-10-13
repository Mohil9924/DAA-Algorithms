class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            # Find the index of the maximum value in the range [left, right]
            max_idx = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            
            root = TreeNode(nums[max_idx])
            root.left = build(left, max_idx - 1)
            root.right = build(max_idx + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)