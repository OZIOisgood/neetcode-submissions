class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                r, l = stack.pop(), stack.pop()
                stack.append(l + r)
            elif c == "-":
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif c == "*":
                r, l = stack.pop(), stack.pop()
                stack.append(l * r)
            elif c == "/":
                r, l = stack.pop(), stack.pop()
                stack.append(int(float(l) / r))
            else:
                stack.append(int(c))
        
        return stack[0]