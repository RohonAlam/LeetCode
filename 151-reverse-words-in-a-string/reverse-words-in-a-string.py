class Solution:
    def reverseWords(self, s: str) -> str:
        """
        # the below solution is acceptable but , can potentially be of O(n2),because of ans += word + " " , it copies the whole string everytime.
        words = s.split()
        ans =""
        for word in words[::-1]:
            ans += word + " "
        return ans.strip()

        """
        return " ".join(s.split()[::-1])


        