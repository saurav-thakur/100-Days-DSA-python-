class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
		
		n = len(str)
		dp = [[0]*(n+1) for i in range(n+1)]
		
		for i in range(len(str)):
		    for j in range(len(str)):
		        if str[i] == str[j] and i!=j:
		            dp[i+1][j+1] = 1 + dp[i][j]
		            
		        else:
		            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
		            
	    return dp[-1][-1]
		