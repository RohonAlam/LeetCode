class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute Force
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
"""



        # Find Row and Binary Search
        rows = len(matrix)

        left = 0
        right = rows - 1

        while left <= right:
            row = left + (right - left) // 2

            if target < matrix[row][0]:
                right = row - 1

            elif target > matrix[row][-1]:
                left = row + 1

            else:
                for num in matrix[row]:
                    if num == target:
                        return True
                return False

        return False       