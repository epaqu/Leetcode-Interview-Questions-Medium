class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """    
        need = [amount+1] * (amount+1)
        need[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                need[i] = min(need[i], need[i - coin] + 1)
        if need[amount] > amount:
            return -1
        return need[amount]
