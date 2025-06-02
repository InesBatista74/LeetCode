class Solution(object):
    def isPalindrome(self, x):
        lista = [] 
        x = str(x)
        x_inverso = str(x)[::-1]
        return x == x_inverso   
        