from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
#3
        directions = [[1,0],[-1,0], [0,1], [0,-1]]

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                
                if grid[r][c] == 0:
                    q.append((r,c))
        distance = 1
        while q:
            length = len(q)

            for i in range(length):
                row, col = q.popleft()

                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0 and grid[nr][nc] == INF:
                        grid[nr][nc] = distance
                        q.append((nr,nc))
                
            distance += 1




                    


                    

