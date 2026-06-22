class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #initialise max profit
        max_profit = 0

        #initialise min price
        min_price = prices[0]

        #iterate over the prices list
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                #update the max profit price
                max_profit = max(max_profit, price - min_price)
        return max_profit
