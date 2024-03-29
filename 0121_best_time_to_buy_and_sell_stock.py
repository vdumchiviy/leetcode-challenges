'''
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must 
buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 10**5
0 <= prices[i] <= 10**4
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = max_price = prices[-1]

        for price in prices[-1::-1]:
            if price > max_price:
                max_price = price
                min_price = price

            if price < min_price:
                min_price = price
                result = max(result, max_price-min_price)

        return result


sol = Solution()

assert sol.maxProfit([7, 2, 9, 1, 5, 0]) == 7
assert sol.maxProfit([7, 2, 9, 1, 5, 15]) == 14
assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit([7, 6, 5, 4, 3, 2, 1]) == 0
assert sol.maxProfit([7]) == 0
assert sol.maxProfit([0, 1, 2, 3, 4, 6]) == 6
assert sol.maxProfit([0, 1, 9, 0, 4, 6]) == 9
assert sol.maxProfit([7, 6, 5, 4, 3, 2, 1, 0]) == 0
assert sol.maxProfit([7, 6]) == 0
assert sol.maxProfit([6, 7]) == 1
