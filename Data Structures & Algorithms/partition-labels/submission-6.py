class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {} # char: last_index

        for i in range(len(s)):
            c = s[i]
            last[c] = i
        
        res = []
        size = end = 0

        for i in range(len(s)):
            c = s[i]
            size += 1

            if last[c] > end:
                end = last[c]
            
            if i == end:
                res.append(size)
                size = 0
        
        return res
