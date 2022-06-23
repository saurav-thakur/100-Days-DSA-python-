# https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1

from heapq import heappush,heapify,heappop

def kthSmallest(mat, n, k): 
    # Your code goes here
    
    heap = []
    heapify(heap)
    
    for i in mat:
        for j in i:
            
            heappush(heap,-1*j)
            
            if len(heap) > k:
                heappop(heap)
                
    return heap[0]*-1