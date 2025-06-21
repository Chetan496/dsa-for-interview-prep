#prob statement https://neetcode.io/problems/buy-and-sell-crypto
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        listsize = len(prices)
        while r < listsize:
            print("l is {}, r is {}".format(l, r))
            left = prices[l]
            right = prices[r]

            if left >= right:
                r = r + 1
            else:
                newProfit = right - left
                if maxProfit < newProfit:
                    maxProfit = newProfit
                r = r + 1

            if r == listsize:
                l = l + 1
                r = l + 1

        return maxProfit


if __name__ == "__main__":
    solution = Solution()
    prices = [1, 2, 4]
    maxProfit = solution.maxProfit(prices)
    print("the maxprofit is {}".format(maxProfit))
