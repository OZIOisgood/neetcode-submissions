class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        for current_parenthese in s:
            if current_parenthese in open_close:
                stack.append(current_parenthese)
            else:
                if stack and open_close[stack[-1]] == current_parenthese:
                    stack.pop()
                else:
                    return False

        is_empty = not stack
        
        return is_empty