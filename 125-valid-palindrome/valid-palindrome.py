class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first apprach is to use another clean string and then check for palindrome
        """
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        
        return clean == clean[::-1]
        """
        # Second approach is to check in the same string , just use two pointers and skip the non alphanumeric characters .

        left = 0
        right = len(s)-1

        while left < right :
            # skip the left characters which is not alphanumeric 

            while left <right and not s[left].isalnum() :
                left += 1
            while left < right and not s[right].isalnum() :
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True