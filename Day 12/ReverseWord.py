# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/0/?track=md-string&batchId=144#

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        
        new_s = S.split(".")
        
        i = 0
        j = len(new_s) - 1
        
        while i <= j:
            new_s[i],new_s[j] = new_s[j],new_s[i]
            i+=1
            j-=1
            
        return ".".join(new_s)