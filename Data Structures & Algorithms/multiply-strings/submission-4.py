class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0

        nums = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        for i, v in enumerate(num1):
            n1 *= 10 # ** (i + 1)
            n1 += nums[v]

        for i, v in enumerate(num2):
            n2 *= 10 # ** (i + 1)
            n2 += nums[v]

        print(n1)
        print(n2)

        return str(n1 * n2)

