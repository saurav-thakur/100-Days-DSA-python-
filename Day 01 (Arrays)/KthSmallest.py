# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1


class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]

from heapq import heapify,heappop,heappush

def kth_smallest(nums,k):

    heap = []
    heapify(heap)

    for i in nums:
        heappush(heap,-1*i)

        if len(heap) > k:
            heappop(heap)

    return heap[0]*-1

nums = [4,2,1,5,3,7,8,0]
k = 3
print(kth_smallest(nums,k))