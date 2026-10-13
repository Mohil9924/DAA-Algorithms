class Solution:
    def specialGrid(self, n: int) -> list[list[int]]:
        size = 1 << n  # 2^n
        grid = [[0] * size for _ in range(size)]
        
        def fill(r: int, c: int, n: int, val: int):
            if n == 0:
                grid[r][c] = val
                return
            
            half = 1 << (n - 1)          # 2^(n-1)
            quad_size = 1 << (2 * n - 2) # 4^(n-1)
            
            # 1. Top-Right (smallest)
            fill(r, c + half, n - 1, val)
            
            # 2. Bottom-Right
            fill(r + half, c + half, n - 1, val + quad_size)
            
            # 3. Bottom-Left
            fill(r + half, c, n - 1, val + 2 * quad_size)
            
            # 4. Top-Left (largest)
            fill(r, c, n - 1, val + 3 * quad_size)
            
        fill(0, 0, n, 0)
        return grid