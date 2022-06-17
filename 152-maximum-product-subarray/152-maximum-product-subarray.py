class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
# dynamic programming
# brutoforce involve going through every subarray and may cost o(n^2)
# consequtive negatives alternate the sixe and return higher value
# we compute max and minimum of the producs in subarray
# edge case is if there is a zero then we resset our prodcut to one to avoid killing the array
        result =max(nums)
        currentMin,currentMax = 1,1
        
        
        for number in nums:
            if number == 0:
                currentMin, currentMax =1,1
                continue
            temporayMax = currentMax * number
            currentMax =max(number * currentMax, number* currentMin, number) #currentMin is used to accomodate negatives since number could be ngeative therefore having it's max is a bonus
            currentMin =min(temporayMax, number* currentMin, number)
            result = max(result,currentMax)
            
        return result
    
    
#     time complexity = O(n) only iterating in input
# space comlexity = O(1) no use of array 
                
                
             
            
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#          #use dynamic progarrming
#         #  let's get arrays which store maximum and minimum
#         length = len(nums)
#         if length < 1:
#             return 0

#         dp_max =[0] * length
#         dp_min =[0] * length
# # we initialize the first value of the array to e the first number

#         dp_min[0]=dp_max[0]=nums[0]
#         # we go through a loop

#         for i in range (1,length):
#             # we check if the number is posiive and we multiply previus dp max to it
#             if nums[i]>0:

#                 dp_max[i] = max(dp_max[i-1]*nums[i],nums[i])

#                 # we also need to store min
#                 dp_min[i] = min(dp_min[i-1]*nums[i],nums[i])

#             else:  #this is when number is negative <0 and will switch betweenmax and min
#                 dp_max[i] = max(dp_min[i-1]*nums[i],nums[i])
#                 dp_min[i] = min(dp_max[i-1]*nums[i],nums[i])
                
                
                
# #                 negative value flip understanding


#         return max(dp_max)



        


        
         