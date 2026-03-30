DIGIT_TO_CHAR = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "qprs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        res = []
        path = []
        
        def bt(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for n in DIGIT_TO_CHAR[digits[i]]:
                path.append(n)
                bt(i + 1)
                path.pop()
                
        bt(0)
        return res