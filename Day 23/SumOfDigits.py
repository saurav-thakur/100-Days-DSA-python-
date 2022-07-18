# https://practice.geeksforgeeks.org/problems/sum-of-digits-of-a-number/0/?track=DSASP-Recursion&batchId=398

class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here
        if n == 0:
            return 0
        
        return n%10 + self.sumOfDigits(n//10)