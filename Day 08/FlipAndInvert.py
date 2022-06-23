# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        
        for i in image:
            temp = [1 if x==0 else 0 for x in i[::-1]]
            res.append(temp)
            
        return res