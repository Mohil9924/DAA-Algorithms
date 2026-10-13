class Solution(object):
    def minimumOperations(self, grid):
        m = len(grid)
        n = len(grid[0])
        operations = 0
        
        # Process each column independently
        for j in range(n):
            for i in range(1, m):
                # If the current element is not strictly greater than the element above it
                if grid[i][j] <= grid[i - 1][j]:
                    # Minimum value grid[i][j] needs to be is grid[i - 1][j] + 1
                    target = grid[i - 1][j] + 1
                    operations += target - grid[i][j]
                    # Update grid[i][j] to target for subsequent row comparisons in this column
                    grid[i][j] = target
                    
        return operations