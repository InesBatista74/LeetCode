class Solution(object):
    def findTheDifference(self, s, t):
        sx = [x for x in s]
        tx = [x for x in t]
        for i in tx:
            if i in sx:
                sx.remove(i)
            else:
                return i
        