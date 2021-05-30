# Very simple solution
class Solution(object):
    def merge(self, n1, m, n2, n):
        n1[m:] = n2
        n1.sort()
