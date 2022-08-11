class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        
        for word in strs:
               
            
            
            key = "".join (sorted(list(word)))
            lookup[key].append(word)
        output=[]                   
        for lists in lookup.values():
            output.append(lists)
                           
        return output
            
        
        
        
        
# Time o(o(n^2))
                           
                           
            
        