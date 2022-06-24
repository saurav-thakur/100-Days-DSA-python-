# https://practice.geeksforgeeks.org/problems/palindrome-string0817/1

class Solution:
	def isPalindrome(self, S):
		# code here
		
		i = 0
		j = len(S) - 1
		
		while i <= j:
		    if S[i]!=S[j]:
		        return 0
		    i+=1
		    j-=1
		return 1