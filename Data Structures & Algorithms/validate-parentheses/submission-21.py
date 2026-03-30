CLOSE_OPEN_PARANTHESES = {
    ')': '(',
    ']': '[',
    '}': '{',
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in CLOSE_OPEN_PARANTHESES:
                if not stack or stack[-1] != CLOSE_OPEN_PARANTHESES[c]: return False
                stack.pop()
            else: stack.append(c)
        return len(stack) == 0