class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res    
    
    
    # using the xor function
    # o{n} time and O(1) space