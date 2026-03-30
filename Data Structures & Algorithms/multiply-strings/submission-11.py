class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]: return "0"


        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)
        n1, n2 = num1[::-1], num2[::-1]
        
        for i1 in range(l1):
            for i2 in range(l2):
                i = i1 + i2
                digit = int(n1[i1]) * int(n2[i2])
                tmp = res[i] + digit
                res[i + 1] += tmp // 10
                res[i] = tmp % 10
        
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0: beg += 1
        
        res = map(str, res[beg:])  

        return "".join(res)