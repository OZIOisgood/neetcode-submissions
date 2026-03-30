class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]
        res = ""

        l = 0; r = len(vals) - 1
        while l <= r:
            m_idx = l + (r - l) // 2
            m_ts, m_val = vals[m_idx]

            if m_ts == timestamp:
                return m_val

            if m_ts < timestamp:
                res = m_val
                l = m_idx + 1
            else:
                r = m_idx - 1

        return res