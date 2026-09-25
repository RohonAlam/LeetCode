class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        #Solved the problem but time limit exceeded
        """

        def wordcheck(word):
            if word in wordDict :
                return True
            
            for i in range(1,len(word)) :
                if word[0:i] in wordDict and wordcheck(word[i:]) :
                    return True
            
            return False
        
        return wordcheck(s)
        """

        wordDict = set(wordDict)
        memo = {}

        def wordcheck(word):
            if word in memo:
                return memo[word]
            if word in wordDict :
                memo[word] = True
                return True
            
            for i in range(1,len(word)) :

                if word[:i] in wordDict and wordcheck(word[i:]) :
                    memo[word] = True
                    return True
            
            memo[word] = False
            return False
        
        return wordcheck(s)
        