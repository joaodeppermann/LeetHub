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
                return 0
            if remainder < 0:
                return None
            
            # Check all the coins and try to minimize return value
            min_coins = +inf
            for coin in coins:
                ret = dfs(remainder - coin)
                if ret is not None:
                    min_coins = min(min_coins, ret + 1)
            
            cache[remainder] = min_coins if min_coins != +inf else None
            return cache[remainder]
        
        dfs(amount)
        return cache[amount] if cache[amount] is not None else -1
                