from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0


        def bfs(r, c):
            q = deque()
            q.append((r,c))

            while q:
                
                r, c = q.popleft()
                grid[r][c] = '-1'
                if (r+1) < rows and grid[r+1][c] == '1':
                    q.append((r+1,c))
                if (r-1) >= 0 and grid[r-1][c] == '1':
                    q.append((r-1,c))
                if (c-1) >= 0 and grid[r][c-1] == '1':
                    q.append((r,c-1))
                if (c+1) < cols and grid[r][c+1] == '1':
                    q.append((r,c+1))

                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        return islands