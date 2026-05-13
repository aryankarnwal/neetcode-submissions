class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[ROWS][COLS];
        int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};

        for (int r = 0 ; r < ROWS ; r++){
            for (int c = 0 ; c < COLS ; c++){
                if (grid[r][c] == 0){
                    q.add(new int[]{r,c});
                    visited[r][c] = false;
                }
            }
        }

        int dist = 1;
        while(q.size()>0){
            int size = q.size();
            for (int i = 0 ; i < size ; i++){
                int[] cur = q.poll();
                int r = cur[0], c = cur[1];

                for (int[] dir : directions){
                    int newR = r + dir[0], newC = c + dir[1];
                    int[] cord = {newR, newC};
                    if (newR < ROWS && newR >= 0 && newC < COLS && newC >=0 && !visited[newR][newC] && grid[newR][newC] == 2147483647){
                        grid[newR][newC] = dist;
                        q.add(cord);
                        visited[newR][newC] = true;
                    }
                }

            }
            dist += 1;
        }



    }
}
