class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                ans.append(path.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates is sorted, everything after this
                # will also be too large
                if candidates[i] > remaining:
                    break

                # Choose
                path.append(candidates[i])

                # i + 1 because each element can be used only once
                backtrack(i + 1, remaining - candidates[i])

                # Undo choice
                path.pop()

        backtrack(0, target)

        return ans