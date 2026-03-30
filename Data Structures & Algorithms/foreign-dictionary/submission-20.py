class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set("".join(words))

        adj = defaultdict(set)
        for i in range(len(words) - 1):
            w1 = words[i]; w2 = words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2: return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        state = defaultdict(int)
        res = []

        def dfs(c: str) -> bool:
            if state[c] == 1:
                return True
            if state[c] == 2:
                return False

            state[c] = 1
            for nei in adj[c]:  # safe even if c not in adj yet
                if dfs(nei):
                    return True

            state[c] = 2
            res.append(c)
            return False

        for c in chars:
            if not state[c] and dfs(c):
                return ""

        res.reverse()
        return "".join(res)