class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack = []

        for ch in s :
            if not stack :
                stack.append(ch)
            else:
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)==0
"""
    #Better logics and return false with first condition break
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            else:
                if not stack:
                    return False

                elif ch == ')' and stack[-1] != '(':
                    return False

                elif ch == '}' and stack[-1] != '{':
                    return False

                elif ch == ']' and stack[-1] != '[':
                    return False

                stack.pop()

        return len(stack) == 0       