class Solution:
    def hammingWeight(self, n: int) -> int:
        result= 0
        
        while n:
            result +=n%2
            n=n>>1
            
        return result
# time 0(32) =0(1)
# space0(1)