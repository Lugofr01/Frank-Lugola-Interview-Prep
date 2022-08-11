class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) #hashmap for mapping character count 
        
        for string in strs:
            count =[0]*26 #a.......z
            
            
            for char in string:
                
# we go through ecvery character in the string
                count[ord(char)- ord("a")] +=1
            result[tuple(count)].append(string) 
        
        
        
        
        return result.values()
           
                
            
        # complexity o(m*n)
        
        
#         lookup = defaultdict(list)
        
#         for word in strs:
               
            
            
#             key = "".join (sorted(list(word)))
#             lookup[key].append(word)
#         output=[]                   
#         for lists in lookup.values():
#             output.append(lists)
                           
#         return output
            
        
        
        
        
# Time o(o(n^2))
                           
                           
            
        