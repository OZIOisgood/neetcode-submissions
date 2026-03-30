class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        
        q = deque([(0, src, 0)]) # price, node, stops
        while q:
            price, node, stops = q.popleft()
            
            if stops > k: continue
            
            for nei_node, nei_price in adj[node]:
                nextPrice = price + nei_price

                if nextPrice < prices[nei_node]:
                    prices[nei_node] = nextPrice
                    q.append((nextPrice, nei_node, stops + 1))
            
        return prices[dst] if prices[dst] != float("inf") else -1