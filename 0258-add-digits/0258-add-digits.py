class Solution(object):
    def addDigits(self, num):
        num = str(num)
        x = [x for x in num] 
        total = 0
        for i in range(len(x)):
            total += int(x[i])
        
        while total > 9:
            total = sum(int(d) for d in str(total))
        return total     