# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here

		count_max = 0

		rowAns = -1
		
		for i in range(n):
		    count_ones = 0
		    
		    for j in range(m):
		        
		        if arr[i][j] == 1:
		            count_ones +=1
		            
		    if count_ones > count_max:
		        count_max = count_ones
		        rowAns = i
		        
	    return rowAns
		