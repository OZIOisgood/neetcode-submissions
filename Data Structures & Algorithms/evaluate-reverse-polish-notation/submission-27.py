ACTIONS = {"+","-","*","/"}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in ACTIONS:
                b = s.pop(); a = s.pop()
                
                match t:
                    case "+": s.append(a + b)
                    case "-": s.append(a - b)
                    case "*": s.append(a * b)
                    case "/": s.append(int(a / b))
            else: s.append(int(t))

        return s[0]