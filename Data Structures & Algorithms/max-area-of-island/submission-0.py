class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[1,0],[-1,0], [0,1],[0,-1]]
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            total = 0
            
            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr >= rows or nr < 0 or nc >= cols or nc < 0 or grid[nr][nc] == 0:
                    continue
                total += dfs(nr, nc)
            return total + 1



        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area