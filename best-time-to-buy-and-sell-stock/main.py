prices1 = [7, 1, 5, 3, 6, 4]  # 5
prices2 = [2, 4, 1]  # 2


class Solution(object):

    # The brutforce algorithm
    def maxProfitBF(self, prices):
        highest = 0

        for i in range(len(prices)):
            profit = 0
            for j in range(i+1, len(prices)):
                sub = prices[j] - prices[i]
                if sub > profit:
                    profit = sub
            if profit > highest:
                highest = profit

        return highest

    def maxProfitKadane(self, prices):
        profit = 0
        buy = prices[0]

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit


sol = Solution()
print(sol.maxProfitKadane(prices1))
print(sol.maxProfitKadane(prices2))
