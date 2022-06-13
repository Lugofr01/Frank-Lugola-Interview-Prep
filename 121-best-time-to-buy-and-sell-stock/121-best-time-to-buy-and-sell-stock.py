class Solution(object):
    def maxProfit(self, prices):
        
        """
        :type prices: List[int]
        :rtype: int
        """
# Aim is to buy low and sell high
# Implement through two pointers, moving to the left and right respectfully
# Left is the day we buy and Right pointer is the day we sell
# If L<R, we move the left pointers to the right and the right becomes the left pointer
# if there is profit we store the profit and move to the next to see if there is a bigger value we update the mex profit, if not we move one
# Memoery is O(1) since we used pointers and no arrays, 
# Time is linear O(n), we scan in array one time
        left,right = 0, 1         #Left is buy, right is sell 

        maxProfit = 0
        
        
        while (right < len(prices)):
            
#             iterating through our prices and we check if it's profitable
            if prices[left]<prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
#             if not a profitable transcation we then update pur left pointer
            else:
#         
                left = right
            
#             also the right pointer gets updated regardless of the conditons and therefore

            right +=1
        return maxProfit
            
                    
        