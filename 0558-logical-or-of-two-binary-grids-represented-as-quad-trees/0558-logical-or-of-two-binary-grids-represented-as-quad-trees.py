class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Base Cases
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        # Recursive Step
        top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # Merge check
        if (top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and
                top_left.val == top_right.val == bottom_left.val == bottom_right.val):
            return Node(top_left.val, True, None, None, None, None)

        return Node(False, False, top_left, top_right, bottom_left, bottom_right)