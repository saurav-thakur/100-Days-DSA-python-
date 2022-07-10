class Solution:
    def maxArea(self,M):
        # code here
        r = len(M)
        c = len(M[0])
        ans = []
        max_ans = 0
        
        for j in range(c):
            ans.append(M[0][j])
        
        for i in range(r):
            for j in range(c):
                if M[i][j] == 0:
                    ans[j] = 0
                    
                else:
                    ans[j] += M[i][j]
                    
            max_ans = max(max_ans,self.max_area_hist(ans))
        return max_ans
        
    def nearest_small_left(self,nums):
        stack = []
        ans = []
        pseudoIdx = -1
        for i in range(len(nums)):
            if len(stack) == 0:
                ans.append(pseudoIdx)
                
            elif len(stack) > 0 and stack[-1][0] < nums[i]:
                ans.append(stack[-1][1])
                
            elif len(stack) > 0 and stack[-1][0] >= nums[i]:
                
                while len(stack) == 0 and stack[-1][0] >= nums[i]:
                    stack.pop()
                    
                if len(stack) == 0:
                    ans.append(pseudoIdx)
                else:
                    ans.append(stack[-1][1])
                    
            stack.append((nums[i],i))
            
        return ans
        
    def nearest_small_right(self,nums):
        stack = []
        ans = []
        pseudoIdx = len(nums)
        for i in range(len(nums)-1,-1,-1):
            if len(stack) == 0:
                ans.append(pseudoIdx)
                
            elif len(stack) > 0 and stack[-1][0] < nums[i]:
                ans.append(stack[-1][1])
                
            elif len(stack) > 0 and stack[-1][0] >= nums[i]:
                
                while len(stack) == 0 and stack[-1][0] >= nums[i]:
                    stack.pop()
                    
                if len(stack) == 0:
                    ans.append(pseudoIdx)
                else:
                    ans.append(stack[-1][1])
                    
            stack.append((nums[i],i))
        ans.reverse()
            
        return ans
        
    def max_area_hist(self,nums):
        right = self.nearest_small_right(nums)
        left = self.nearest_small_left(nums)
        max_area = 0
        width = []
        print(right)
        print(left)
        
        for i in range(len(nums)):
            width.append(right[i]-left[i]-1)
        
        for i in range(len(nums)):
            area = width[i]*nums[i]
            max_area = max(area,max_area)
            
        return max_area
        
s = Solution()
mat = [[0,1,1,0],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0]]
print(s.maxArea(mat))