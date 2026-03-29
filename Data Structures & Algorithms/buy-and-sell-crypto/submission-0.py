class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to get min and max values to get max profit

        # need to get it chronologically 

        #two pointer problem 
        #left day one, right day two , left buy, right sell 
        # if right less then left, update pointer to right is left, 

        #update max profit
        #can leave left pointer and update only right as long as right is greater than left
        # two pointer is o(n), memory is o(1)

        l, r = 0, 1 #left buy, right sell
        maxprofit = 0


        while r < len(prices): 
            #profitable? -> if left pointer is less than right
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit) # check max of current and one we are checking
            else: 
                l = r # shift to the new low
            
            r+=1
        return maxprofit





        
        