class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        for c in s:
            if c in closeOpen:
                stack.append(c)
            else:
                if stack and closeOpen[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False