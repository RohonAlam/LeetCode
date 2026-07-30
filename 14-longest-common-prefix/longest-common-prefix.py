class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical Scanning (Optimal)
        """
        min_len  = min (len(s) for s in strs)
        last = 0 
        for i in range(min_len):           # Fix 1
            ch = strs[0][i]
            for s in strs:                 # Check ALL strings including strs[0]
                if len(s) <= i or ch != s[i]:
                    return strs[0][:i]     # Fix 2: break early + correct slice
        return strs[0][:min_len]           # Fix 3: full prefix case
        """
        """
        strs.sort()
        if not strs :
            return ""
        first = strs[0]
        last = strs[-1]
        min_len = min(len(first),len(last))

        for i in range(min_len):
            if first[i] != last[i] :
                return first[:i]
        return  first[:min_len]
        """
        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0
        
        while i<len(first) and i < len(last) and first[i] == last[i] :
            i += 1

        return first[:i] 