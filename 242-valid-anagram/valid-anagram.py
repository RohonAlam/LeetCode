class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using Counter from collections
        """
        from collections import Counter
        return Counter(s) == Counter(t)
"""
        # we can also use a constant array of size 256 , check all character freq and compare the arrays 

        # using Sorting
        # return sorted(s) == sorted(t)
       
        # Using a HASH MAP
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:

            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
        
        