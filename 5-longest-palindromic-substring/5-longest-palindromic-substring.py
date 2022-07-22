class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    
    
    
    
#     TIME IS ON2 BUT SPACE IS O(N)









        
        
        
        
        
        
#         result =""
#         resultLength = 0
        
        
#         for i in range (len(s)):
            
#             #odd length edge case
#             left,right= i,i
#             # i is the center 
#             while left>=0 and right <len(s) and s[left]==s[right]:
#                 # we check if the result length
#                 if (right-left +1)>resultLength:
#                     result = s[left:right+1]
#                     resultLength = right-left +1
#                 left-=1
#                 right+=1
                
#             #even length edge case
#             left,right= i,i+1
#             # i is the center 
#             while left>=0 and right <len(s) and s[left]==s[right]:
#                 # we check if the result length
#                 if (right-left +1)>resultLength:
#                     result = s[left:right+1]
#                     resultLength = right-left +1
#                 left-=1
#                 right+=1
                
#         return result
                
            
                
#             # complexity is 0(n^3)

            
        