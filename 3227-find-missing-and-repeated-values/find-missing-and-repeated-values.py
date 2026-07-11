class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #Brute Force
        # n = len(grid)
        # repeated = missing = -1

        # for num in range(1, n * n + 1):
        #     cnt = 0
        #     for row in grid:
        #         for val in row:
        #             if val == num:
        #                 cnt += 1

        #     if cnt == 2:
        #         repeated = num
        #     elif cnt == 0:
        #         missing = num

        # return [repeated, missing]

        # Hash Map/ Frequesncy Array
        # n = len(grid)
        # freq = [0]* (n*n+1)
        # repeated = missing = -1

        # for row in grid:
        #     for val in row:
        #         freq[val] += 1

        # for num in range(1,n*n+1):
        #     if freq[num] == 2:
        #         repeated = num
        #     elif freq[num] == 0:
        #         missing = num
        # return [repeated, missing]

        #Mathematical Solution
        # n = len(grid)
        # N = n * n

        # expected_sum = N * (N + 1) // 2
        # expected_sq = N * (N + 1) * (2 * N + 1) // 6

        # actual_sum = 0
        # actual_sq = 0

        # for row in grid:
        #     for num in row:
        #         actual_sum += num
        #         actual_sq += num * num

        # diff = expected_sum - actual_sum          # missing - repeated
        # sq_diff = expected_sq - actual_sq

        # sum_xy = sq_diff // diff

        # missing = (diff + sum_xy) // 2
        # repeated = sum_xy - missing

        # return [repeated, missing]

        #using Set
        a =0
        b=0 
        nums = [x for row in grid for x in row]
        n = len(nums)
        s = set()
        for num in nums:
            if num in s:
                a = num
            s.add(num)
        b = (n * (n+1) // 2 ) - sum(s) 
        return [a,b]
