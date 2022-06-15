# https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1

class Solution:
    def rearrange(self,arr, n):
        # code here
        pos = []
        neg = []
        final_ans = []
        for i in arr:
            if i < 0:
                neg.append(i)
                
            else:
                pos.append(i)
        
        x = y = z = 0
        
        while x < len(pos) and y < len(neg):
            arr[z] = pos[x]
            z+=1
            x+=1
            
            arr[z] = neg[y]
            z+=1
            y+=1
            
            
        while x < len(pos):
            arr[z] = pos[x]
            z+=1
            x+=1
        
        while y < len(neg):
            arr[z] = neg[y]
            z+=1
            y+=1