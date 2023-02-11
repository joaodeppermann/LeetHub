class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # divide and conquer 
        # divide original arr into two subsequences and calc max profit for each subsequence
        
        # one array keeping res from left to right
        # other array keeping results from right to left
        
        # get the best profits "cruzados" and sum them up 

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         t1_cost, t2_cost = float('inf'), float('inf')
#         t1_profit, t2_profit = 0, 0

#         for price in prices:
#             # the maximum profit if only one transaction is allowed
#             t1_cost = min(t1_cost, price)
#             t1_profit = max(t1_profit, price - t1_cost)
#             # reinvest the gained profit in the second transaction
#             t2_cost = min(t2_cost, price - t1_profit)
#             t2_profit = max(t2_profit, price - t2_cost)

#         return t2_profit
        