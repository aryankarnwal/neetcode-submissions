from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        time = 0
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh:
            time += 1
            qlen = len(q)

            for i in range(qlen):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh.remove((nr,nc))
                        q.append((nr,nc))
        
        if fresh:
            return -1
        return time
        


                
        

