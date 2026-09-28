class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(r,c,pr,pc,val):
            visited[r][c] = True
            for dr,dc in directions :
                nr , nc = r + dr , c + dc

                if 0 <= nr < m and 0<= nc < n and grid[nr][nc] == val :

                    if nr == pr and nc == pc :
                        continue

                    if visited[nr][nc] :
                        return True

                    else :
                        if dfs(nr,nc,r,c,val) :
                            return True

            return False

            
        for i in range(m) :
            for j in range(n) :
                if not visited[i][j]:
                    if dfs(i,j,-1,-1,grid[i][j]) :
                        return True
            
        return False

    # explained version of the code - class Solution:
    """
    def containsCycle(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, pr, pc, val):
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == val:
                    # Skip the cell we just came from (immediate parent)
                    if nr == pr and nc == pc:
                        continue
                    
                    # If the neighbor is already visited, we found a cycle!
                    if visited[nr][nc]:
                        return True
                    
                    # Otherwise, continue DFS into the neighbor
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, val):
                            return True
                            
            return False

        # Iterate through every cell to handle disconnected components
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    # Start DFS with parent set to (-1, -1)
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False

    """

        