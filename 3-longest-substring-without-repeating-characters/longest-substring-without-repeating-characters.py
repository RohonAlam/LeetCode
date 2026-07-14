class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Brute Force
        """
        max_len = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    break

                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len
"""
        #Sliding window + Seen set()
        seen = set()
        left = 0 
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len,right - left +1)

        return max_len

