class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # O(n) solution will involve going through each number in array and checking if it's our target
#         anything better than linear is a binary search solution
# analyse graph pattern in a sorted rotated array
        left = 0
        right = len(nums)-1
        
        
        while left<=right:
            
            mid =(left+right)//2
            if target == nums[mid]:
                return mid
            
#             let's check which portion of array are we in

# left sorted portion
            if nums[left]<=nums[mid]:
                if target > nums[mid] or target <nums[left]:
                    left = mid+1
                    
#then we search right since the value is not on the left sorted portion
                else:
                    right = mid -1
                
                    
            
                
# right sorted portion is the else
            else:
                if target < nums[mid] or target>nums[right]:
                    right =mid-1
                    # we search left of the array
                else:
                    left =mid +1
                    # we search right part of the array
        return -1  
    
    
    # time o(nlogn) space o(1)
                    
                    
                    
        
                
                
                

                
            
            

        