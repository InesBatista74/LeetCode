class Solution(object):
    def mySqrt(self, x):
        i = 0
        while i * i <= x:
            i += 1
        return i - 1

        