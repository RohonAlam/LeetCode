class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:

        n = len(maze)

        moves = [
            (1, 0, "D"),
            (0, -1, "L"),
            (0, 1, "R"),
            (-1, 0, "U")
        ]

        ans = []
        temp = []

        visited = [[False] * n for _ in range(n)]

        def validMove(row, col):

            # Check boundary
            if row < 0 or row >= n or col < 0 or col >= n:
                return False

            # Blocked cell
            if maze[row][col] == 0:
                return False

            # Already visited
            if visited[row][col]:
                return False

            return True

        def backtrack(row, col):

            # Destination reached
            if row == n - 1 and col == n - 1:
                ans.append("".join(temp))
                return

            # Mark current cell visited
            visited[row][col] = True

            for r, c, move in moves:

                newRow = row + r
                newCol = col + c

                if validMove(newRow, newCol):

                    # Choose
                    temp.append(move)

                    # Explore
                    backtrack(newRow, newCol)

                    # Undo
                    temp.pop()

            # Backtrack from current cell
            visited[row][col] = False

        # Starting or destination cell blocked
        if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return []

        backtrack(0, 0)

        return ans