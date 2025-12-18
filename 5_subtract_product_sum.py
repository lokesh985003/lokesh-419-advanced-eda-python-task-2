class Solution(object):
    def subtractProductAndSum(self, n):
        a = str(n)     
        b = 0           
        c = 1          
        for i in a:
            x = int(i)
            b = b + x
            c = c * x
        return c - b
