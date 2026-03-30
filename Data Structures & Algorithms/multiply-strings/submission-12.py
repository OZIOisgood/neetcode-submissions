class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"

        # num1 is greater or equal and revert both
        num1, num2 = (num1[::-1], num2[::-1]) if len(num1) >= len(num2) else (num2[::-1], num1[::-1])
        n1, n2 = num1, num2
        l1, l2 = len(n1), len(n2)

        # prepare a place for a res
        res = [0] * (l1 + l2)

        # multiply + carry directly into res
        for i1 in range(l1):
            for i2 in range(l2):
                i = i1 + i2
                digit = (ord(n1[i1]) - ord('0')) * (ord(n2[i2]) - ord('0'))
                tmp = res[i] + digit
                res[i + 1] += tmp // 10
                res[i] = tmp % 10

        # revert
        res, beg = res[::-1], 0

        # trim
        while beg < len(res) and res[beg] == 0: beg += 1
        if beg == len(res): return "0"

        return "".join(str(d) for d in res[beg:])