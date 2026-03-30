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

        return not stack

        # if not stack:
        #     return True
        # else:
        #     return False

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