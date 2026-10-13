class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        
        # Build the Fenwick Tree
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, index: int, val: int) -> None:
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)

    def _query(self, index: int) -> int:
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & (-index)
        return sum_val

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)