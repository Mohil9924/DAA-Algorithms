class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        def heapify(length: int, root: int):
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            # Check if left child exists and is greater than root
            if left < length and nums[left] > nums[largest]:
                largest = left

            # Check if right child exists and is greater than largest so far
            if right < length and nums[right] > nums[largest]:
                largest = right

            # If largest is not root, swap and continue heapifying
            if largest != root:
                nums[root], nums[largest] = nums[largest], nums[root]
                heapify(length, largest)

        # Build Max-Heap (bottom-up)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Extract elements one by one from heap
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Move current root to end
            heapify(i, 0)                        # Heapify reduced heap

        return nums