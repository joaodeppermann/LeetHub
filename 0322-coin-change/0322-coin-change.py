class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = {}
        path = defaultdict(list)
        def dfs(remainder):
            if remainder in cache:
                return cache[remainder]
            # base cases
            if remainder == 0:
                return (0, [])
            if remainder < 0:
                return (-1, [])
            
            min_coins = +inf
            for coin in coins:
                ret = dfs(remainder - coin)
                ret_num = ret[0]
                ret_path = ret[1]
                if ret_num != -1:
                    if min_coins > ret_num + 1:
                        min_coins = ret_num + 1
                        # Update path using this coins
                        path[remainder] = ret_path.append(coin)
                        
            if not path[remainder]:
                path[remainder] = []
                   
            cache[remainder] = (min_coins, path[remainder])
            return cache[remainder]
        
        dfs(amount)
        return cache[amount][0] if cache[amount][0] != +inf else -1
                