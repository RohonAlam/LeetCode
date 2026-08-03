class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            ans = []
            path = []

            def backtrack(i, remaining):
                if remaining == 0:
                    ans.append(path.copy())
                    return

                if i == len(candidates) or remaining < 0:
                    return

                # Take candidates[i]
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

                # Skip candidates[i]
                backtrack(i + 1, remaining)

            backtrack(0, target)

            return ans