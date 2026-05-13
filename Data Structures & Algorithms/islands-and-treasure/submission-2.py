class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        def bfs():
            
            dist = 0
            while len(q) > 0:
                size = len(q)
                dist += 1
                for i in range(size):
                    
                    r, c = q.popleft()

                    for dr, dc in directions:
                        newR = dr + r
                        newC = dc + c
                        if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 2147483647:

                            grid[newR][newC] = dist
                            q.append([newR, newC])
                        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        bfs()
