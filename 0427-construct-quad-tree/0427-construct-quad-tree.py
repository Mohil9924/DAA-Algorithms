"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(r: int, c: int, size: int) -> 'Node':
            if size == 1:
                return Node(grid[r][c] == 1, True)
            
            half = size // 2
            top_left = solve(r, c, half)
            top_right = solve(r, c + half, half)
            bottom_left = solve(r + half, c, half)
            bottom_right = solve(r + half, c + half, half)
            
            # If all four children are leaf nodes and have the same value, merge them into a leaf
            if (top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and
                top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)
            
            # Otherwise, create an internal node
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
            
        return solve(0, 0, len(grid))