class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i in range(len(nums)):
            result = target - nums[i]
            
            if result in hashmap:
                return (hashmap[result],i)
            hashmap[nums[i]]= i
            
#         Time complexity: O(n)O(n). We traverse the list containing nn elements exactly twice. Since the hash table reduces the lookup time to O(1)O(1), the overall time complexity is O(n)O(n).

# Space complexity: O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.

