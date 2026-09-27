class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        # Solved the question but it will exceed time limit 
        """

        dictionary = set(dictionary)

        def checkString(s):
            if not s:
                return 0

            # Option 1: current character is extra
            res = 1 + checkString(s[1:])

            # Option 2: take a dictionary word
            for i in range(1, len(s) + 1):
                if s[:i] in dictionary:
                    res = min(res, checkString(s[i:]))

            return res

        return checkString(s)
        """

        # solving again with top down dp and memoization 

        dictionary = set(dictionary)

        memo = {}

        n = len(s)

        def dp(start):

            if start == n :
                return 0 
            
            if start in memo :
                return memo[start]
            

            res = 1 + dp(start+1)

            for end in range(start+1,n+1) :
                if s[start:end] in dictionary :
                    res = min(res,dp(end))
            memo[start] = res
            return res
        
        return dp(0)

        """

        # Convert dictionary to a set for O(1) lookups
        dict_set = set(dictionary)
        n = len(s)
        
        # Dictionary to store the minimum extra characters for a given starting index
        memo = {}

        def dp(start):
            # Base case: reached the end of the string, no extra characters left
            if start == n:
                return 0
            
            # Return cached result if we've already solved for this index
            if start in memo:
                return memo[start]

            # Option 1: Treat the current character as an extra character
            # Add 1 to the count and move to the next index
            min_extra = 1 + dp(start + 1)

            # Option 2: Try to form a valid word starting from the current index
            for end in range(start + 1, n + 1):
                if s[start:end] in dict_set:
                    # If it's a valid word, 0 extra characters for this portion
                    # We just take the result of the remaining string
                    min_extra = min(min_extra, dp(end))

            # Cache and return the result
            memo[start] = min_extra
            return min_extra

        return dp(0)
        """
        
    