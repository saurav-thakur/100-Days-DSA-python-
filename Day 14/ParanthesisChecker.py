# https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        
        stack = []
        
        for i in x:
            if i in ["{","[","("]:
                stack.append(i)
                
            else:
                if len(stack) == 0:
                    return False
                
                curr = stack.pop()
                
                if curr == "(":
                    if i!=")":
                        return False
                        
                elif curr == "[":
                    if i!="]":
                        return False
                        
                elif curr == "{":
                    if i!="}":
                        return False
        if not stack:
            return True
        return False