class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       


       #if right < left -> left = right
       # if right - left < max -> right +=1

        left = 0 
        profit = 0

        for i in range(0, len(prices)):
            right = i 
            current = prices[right]-prices[left]
            if current <= 0:
                left = right
            elif current  > profit:
                profit = current
        
        return profit

        







        