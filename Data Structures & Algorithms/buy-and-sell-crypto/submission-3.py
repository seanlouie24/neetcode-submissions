class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        # Two pointers
        # Check if the subtraction > max_proftit
        # If it is replace it
        # Keep track of min_day and only change it if we come across a day cheaper


        min_day = 0

        for i in range(1,len(prices)):
            temp = prices[i] - prices[min_day]
            if temp > max_profit:
                max_profit = temp
            
            if prices[i] < prices[min_day]:
                min_day = i
        
        return max_profit

    
    # O(n)
    # O(1)