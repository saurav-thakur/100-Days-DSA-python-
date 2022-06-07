# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# https://youtu.be/sEQk8xgjx64

class Solution:
    def sort012(self,arr,n):
        # code here
        
        l = 0
        m = 0
        h = len(arr) - 1
        
        while m <= h:
            if arr[m] == 0:
                arr[m],arr[l] = arr[l],arr[m]
                l+=1
                m+=1
                
            elif arr[m] == 1:
                m+=1
                
            elif arr[m] == 2:
                arr[m],arr[h] = arr[h],arr[m]
                h-=1
                
        return arr