class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                l = prices[s] + p

                if l < tmp[d]:
                    tmp[d] = l
            
            prices = tmp
        
        if prices[dst] != float("inf"):
            return prices[dst]
        else:
            return -1
        