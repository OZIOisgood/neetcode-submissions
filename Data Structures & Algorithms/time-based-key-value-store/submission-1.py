class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, val: str, ts: int) -> None:
        self.store[key].append([val, ts])

    def get(self, key: str, ts: int) -> str:
        res = ""
        vals = self.store[key]

        l = 0; r = len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            v, t = vals[m]
            if t <= ts:
                res = v
                l = m + 1
            else:
                r = m - 1
        return res