class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # res = s
        # while part in res :
        #     res = res.replace(part,"")
        # return res

        stack = []
        n = len(s)
        m = len(part)
        for ch in s:
            stack.append(ch)

            if len(stack)>=m and "".join(stack[-m:]) == part:
                del stack[-m:]
        return "".join(stack[:])