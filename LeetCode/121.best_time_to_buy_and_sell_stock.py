def max_profit(prices):
	  if not prices:
        return 0
    max_profit, min_price = 0, prices[0]
    for price in prices:
        min_price = price if price < min_price else min_price
        max_profit = price - min_price if price - \
            min_price > max_profit else max_profit
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
