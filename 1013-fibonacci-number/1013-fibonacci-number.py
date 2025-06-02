class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        lst = [0, 1]
        for i in range(2, n+1):
            lst.append(lst[i - 1] + lst[i - 2])
        return lst[n]
        