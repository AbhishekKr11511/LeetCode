'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# Solution 
# Time complexity = O(n)

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    sellingPrices = [0]
    maxselling = 0
    for i in range(len(prices)-1, 0, -1):
        sellingPrices.append(max(maxselling, prices[i]))
        maxselling = max(maxselling, prices[i])
    maxProfit = 0
    for j in range(len(prices)):
        maxProfit = max(sellingPrices[len(prices)-j-1]-prices[j], maxProfit)
    return maxProfit


# Better Solution 
# Time complexity = O(n)
def maxProfit2(prices):
    if len(prices) <=1:
        return 0
    length = len(prices)
    i = 0
    j = i+1
    maxProfit = 0
    while j < length:
        if prices[i] > prices[j]:
            i = j
            j += 1
        else:
            maxProfit = max(maxProfit, prices[j]-prices[i])
            j += 1
    return maxProfit
    
print(maxProfit2([7,1,5,3,6,4]))