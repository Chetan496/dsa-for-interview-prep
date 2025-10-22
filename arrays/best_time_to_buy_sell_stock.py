"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Technique: One Pass / Dynamic Programming
"""

def max_profit(prices):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2, 3, 4, 5],
        [2, 4, 1]
    ]
    
    for prices in test_cases:
        result = max_profit(prices)
        print(f"Input: {prices} -> Output: {result}")
