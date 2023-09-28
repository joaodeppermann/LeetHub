class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case
        if amount == 0:
            return 0
        memo = {}
        def dfs(remainder):
            # Check cache
            if remainder in memo:
                return memo[remainder]
            # Base cases
            if remainder == 0:
                return 0
            if remainder < 0:
                return -1
            
            # Minimize number of coins for this amount/remainder
            min_coins = +inf
            # Check all the coins
            for coin in coins:
                res = dfs(remainder - coin)
                if res != -1:
                    min_coins = min(min_coins, res + 1)
                    
            memo[remainder] = min_coins
            return memo[remainder]
        
        dfs(amount)
        return memo[amount] if memo[amount] != +inf else -1
                