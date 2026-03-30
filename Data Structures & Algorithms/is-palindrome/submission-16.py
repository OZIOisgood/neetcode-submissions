class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            lC, rC = s[l].lower(), s[r].lower()
            
            print(f"lC: '{lC}'; rC: '{rC}'")

            if lC != rC:
                return False

            l += 1; r -= 1

        return True