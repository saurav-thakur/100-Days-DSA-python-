# https://practice.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        
        if len(str1) != len(str2):
            return False
            
        d = {}
        
        for i in range(len(str1)):
            d[str1[i]] = str2[i]
            
        for i in range(len(str1)):
            if str2[i] != d[str1[i]]:
                return False
                
        for i in range(len(str2)):
            d[str2[i]] = str1[i]
            
        for i in range(len(str2)):
            if str1[i] != d[str2[i]]:
                return False
                
        return True