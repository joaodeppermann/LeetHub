class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = {}
        def dfs(remainder):
            if remainder in cache:
                return cache[remainder]
            # base cases
            if remainder == 0:
                return [] # Start building path
            if remainder < 0:
                return None
            
            min_len = +inf
            for coin in coins:
                ret = dfs(remainder - coin)
                if ret is not None:
                    if min_len > len(ret) + 1:
                        min_len = len(ret) + 1
                        best_path = ret.copy()
                        best_path_coin = coin
                        
            if min_len != +inf:
                best_path.append(best_path_coin)
                cache[remainder] = best_path
                return best_path
            
            cache[remainder] = None
            return None
    
    
        dfs(amount)
        print(cache[amount])
        return len(cache[amount]) if cache[amount] != None else -1
                