class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case
        if amount == 0:
            return 0
        cache = {}
        def dfs(remainder):
            # Check cache to avoid repeated work
            if remainder in cache:
                return cache[remainder]
            # Base cases
            if remainder == 0:
                return 0
            if remainder < 0:
                return -1
            
            min_coins = +inf
            for coin in coins:
                ret = dfs(remainder - coin)
                if ret != -1:
                    min_coins = min(min_coins, ret + 1)
                    
            cache[remainder] = min_coins
            return cache[remainder]
        dfs(amount)
        return cache[amount] if cache[amount] != +inf else -1