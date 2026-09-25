class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # USING SORTING
        """
        if not strs :
            return ""
        strs.sort()
        res = 0

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                res += 1
            else :
                break
        
        return strs[0][:res]
        """
        # Vertical Scanning

        if not strs :
            return ""
        
        min_len = min (len(s) for s in strs)

        for i in range(min_len):
            ch = strs[0][i]

            for s in strs :

                if i >= len(s) or s[i] != ch :
                    return strs[0][:i]

        return strs[0][:min_len]        