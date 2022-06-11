# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
# https://youtu.be/Av7vSnPSCtw

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        
        s = arr[0] + k
        l = arr[n-1] - k
        
        ans = arr[n-1] - arr[0]
        
        for i in range(len(arr)-1):
            mi = min(s,arr[i+1]-k)
            mx = max(l,arr[i]+k)
            
            if mi <0:
                continue
            ans = min(ans,mx-mi)
            
            
        return ans