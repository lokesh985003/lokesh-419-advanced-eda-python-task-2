class Solution(object):
    def xorOperation(self, n, start):
        a = 0
        b = start
        for i in range(n):
            c = b + 2 * i
            a = a ^ c
        return a
