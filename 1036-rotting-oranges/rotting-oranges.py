from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2 :
                    queue.append((r,c))
                if grid[r][c] == 1 :
                    fresh += 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue and fresh>0 :

            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft()

                for dr , dc in directions :
                    nr = r + dr 
                    nc = c + dc

                    #check boundaries

                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1 :
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
            minutes += 1

        return minutes if fresh ==0 else -1 





        