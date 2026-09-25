class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        res = 0

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                res += 1
            else :
                break
        
        return strs[0][:res]
        