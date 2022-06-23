from heapq import heapify, heappush, heappop


# Time Complexity - O(N2LogN)
class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        
        heap = []
        heapify(heap)
        
        for i in Mat:
            for j in i:
                heappush(heap,j)
                
        r = 0
        c = 0
        
        while heap:
            Mat[r][c] = heappop(heap)
            c += 1
            
            if c == N:
                r+= 1
                c = 0
                
        return Mat
            