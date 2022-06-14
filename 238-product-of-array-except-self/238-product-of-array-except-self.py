class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#initialzing our result 
        # we dont have to wrry about interger overflow
        #  we need o(n) time and o(1) space
        # we have to multiply evry thing to the left of the chosen index and everything to the right
        # we keep appending after doing operations from the left and right 
        # but if we do this nested in loops we will have on^2 time
        # we multiply prefix and post fix of answer[i] and then combine then and get the desired solution
#        when threre is no prefix or post fix we assume the value of one
        result = [1]   *(len(nums))
        prefix = 1
        
        
        for i in range(len(nums)):
            result[i] = prefix
            
            prefix = prefix * nums[i]
            
        postfix = 1
        
        for i in range(len(nums)-1,-1,-1):
            
#             because we start from the end to the begining therefore 
            result[i] =  result[i] *postfix
#     multiply to avoid overiding the result
            postfix = postfix * nums[i]
    
        return result
    
    
            
            
    
    
#     Memory O(n) time and O(1)  space