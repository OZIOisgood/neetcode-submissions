class Solution:
    def checkValidString(self, s: str) -> bool:
        _min = _max = 0

        for c in s:
            if c == "(":
                _min += 1
                _max += 1
            elif c == ")":
                _min -= 1
                _max -= 1
            elif c == "*":
                _min -= 1
                _max += 1

            if _max < 0:
                return False
            
            _min = max(
                0,
                _min
            )
        
        return not _min

            