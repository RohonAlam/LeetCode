class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        res = defaultdict(int)

        for ch in s: 
            res[ch] += 1
        for i in range(len(s)) :
            if res[s[i]] == 1 :
                return i
        return -1


        