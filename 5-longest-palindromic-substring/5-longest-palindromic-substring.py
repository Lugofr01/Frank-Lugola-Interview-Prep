class Solution:
    def longestPalindrome(self, s: str) -> str:
        result =""
        resultLength = 0
        
        
        for i in range (len(s)):
            
            #odd length edge case
            left,right= i,i
            # i is the center 
            while left>=0 and right <len(s) and s[left]==s[right]:
                # we check if the result length
                if (right-left +1)>resultLength:
                    result = s[left:right+1]
                    resultLength = right-left +1
                left-=1
                right+=1
                
            #even length edge case
            left,right= i,i+1
            # i is the center 
            while left>=0 and right <len(s) and s[left]==s[right]:
                # we check if the result length
                if (right-left +1)>resultLength:
                    result = s[left:right+1]
                    resultLength = right-left +1
                left-=1
                right+=1
                
        return result
                
            
                
            # complexity is 0(n^3)

            
        