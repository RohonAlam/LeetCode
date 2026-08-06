class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        temp = []

        def backtrack(start):
            ans.append(temp.copy())

            for i in range(start, len(nums)):

                # Skip duplicate choices at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Choose
                temp.append(nums[i])

                # Explore
                backtrack(i + 1)

                # Undo
                temp.pop()

        backtrack(0)

        return ans