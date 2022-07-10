class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingBrackets = ['[','{' ,'(']
        
        for i in s:
            if i in openingBrackets:
                stack.append(i)
                
            else:
                
                if len(stack) == 0:
                    return False

                curr = stack.pop()
                
                if i == '}':
                    if curr != '{':
                        return False
                        
                    
                elif i == ']':
                    if curr != '[':
                        return False

                elif i == ')':
                    if curr != '(':
                        return False
                        
        if len(stack) == 0:
            return True
        return False

s = Solution()
print(s.isValid("(])"))