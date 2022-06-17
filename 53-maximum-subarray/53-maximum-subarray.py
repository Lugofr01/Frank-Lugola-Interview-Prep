class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
#         alienate the negatives and ignore them and move right and update the indences that contribite to larger sums
# remove negative prefixes sliding window
        maxSub = nums[0] #first index and it is being initialized
    
        currentSum = 0
        
        for number in nums:  #iterate over the array
            if currentSum<0:#remove negative prefixes
                currentSum = 0
            currentSum += number #the next number in the array is updated
            
            maxSub =max(maxSub,currentSum)  #maximum array maybe the maxSub or the current sum
            
            
            
            
        return maxSub
    
    
#     time complexity O(n) linear and no extra space was needed
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_sum, current_sum = float('-inf'),0
        
# #         we use -inf since it's nitialize a variable maxSubarray = -infinity to keep track of the best subarray. We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.

# # kadons alogirithm

#         for n in nums:
#             current_sum = max(current_sum+n,n)
#             max_sum = max(max_sum,current_sum)

#         return max_sum
    