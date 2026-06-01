class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            letter_index = columnNumber % 26
            res.append(chr(ord('A') + letter_index))
            columnNumber //= 26

        return ''.join(reversed(res))