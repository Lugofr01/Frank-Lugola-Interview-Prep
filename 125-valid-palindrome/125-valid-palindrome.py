class Solution:
    def isPalindrome(self, s):
        
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -= 1
        return True
    def alphaNum(self,char):
        return (ord("A")<=ord(char)<= ord("Z")
        or
        ord("a")<=ord(char)<= ord("z")
        or
        ord("0")<=ord(char)<= ord("9"))
        # we access ascii via ord function\\
        
        
        # O(n) time and O(1) space
        
        
        
        
    

    
    
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr=""
        
        
#         for i in s:
#             if i.isalnum():
#                 newStr+=i.lower()
                
#         return newStr == newStr[::-1]
    
#     # memory is 0(n), and time o(n)
            
                