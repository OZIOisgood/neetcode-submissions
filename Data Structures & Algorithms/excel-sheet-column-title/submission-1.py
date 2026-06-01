class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            latest = columnNumber % 26
            res += alphabet[latest]
            columnNumber //= 26

        return res[::-1]