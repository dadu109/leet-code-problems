prices1 = [7, 1, 5, 3, 6, 4]  # 5
prices2 = [2, 4, 1]  # 2

# The brutforce algorithm


class Solution(object):
    def maxProfit(self, prices):
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


sol = Solution()
print(sol.maxProfit(prices1))
print(sol.maxProfit(prices2))
