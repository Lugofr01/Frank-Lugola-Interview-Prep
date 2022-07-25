class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dic={")":"(","}":"{","]":"["}
        
        for parantheses in s:
            if parantheses in dic.values():
                stack.append(parantheses)
            elif stack and dic[parantheses]==stack[-1]:
                # stack[-1] means stack at the top  
                stack.pop()
                
            else:
                return False
        return stack ==[]
    
    
    # 0(N) time and o(n) space
        
        