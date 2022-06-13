class Solution(object):
    def containsDuplicate(self, nums):
        
        
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
# We could use bruteforce and the space complexity will be O(n^2) with O(1) time
# But if we sort we only have to worry about what's adjacent to the elemtn in the list and therefore have O(nlogn) complexity 

# We can further improve the time complexity by trading off the spacr complexity and this is using a hashset the space will be O(n) and time will be O(1)
        hashset =set()
    
        for n in nums:
            
            if n in hashset:
                return True
            
            else:
                hashset.add(n)
                
        return False
        