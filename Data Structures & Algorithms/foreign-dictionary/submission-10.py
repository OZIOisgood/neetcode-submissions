class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set([c for w in words for c in w])

        adj = defaultdict(set)  # missing keys create empty set automatically

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        state = {c: 0 for c in chars}
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
            if state[c] == 0 and dfs(c):
                return ""

        res.reverse()
        return "".join(res)