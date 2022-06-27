# https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        ans = []
        
        for i in S:
            if ans and ans[-1] != i:
                ans.append(i)
            elif not ans:
                ans.append(i)
                
        return "".join(ans)