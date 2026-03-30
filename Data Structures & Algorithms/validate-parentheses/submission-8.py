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

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         openClose = {
#             "{": "}",
#             "(": ")",
#             "[": "]",
#         }

#         for currentParenthese in s:
#             if currentParenthese in openClose:
#                 stack.append(currentParenthese)
#             else:
#                 lastParenthese = stack[-1]
#                 correspondingClose = openClose[lastParenthese]
#                 if stack and currentParenthese == correspondingClose:
#                     stack.pop()
#                 else:
#                     return False

#         # return not not stack

#         if not stack:
#             return True
#         else:
#             return False