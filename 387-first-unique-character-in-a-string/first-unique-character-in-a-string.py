class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Using default dict
        """
        from collections import defaultdict
        res = defaultdict(int)

        for ch in s: 
            res[ch] += 1
        for i in range(len(s)) :
            if res[s[i]] == 1 :
                return i
        return -1
        """
        # Using Counter()
        from collections import Counter

        count = Counter(s)

        for i , ch in enumerate(s):
            if count[ch] == 1 :
                return i 
        return -1