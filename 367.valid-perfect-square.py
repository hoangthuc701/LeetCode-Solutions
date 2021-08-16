# Author: Nguyen Hoang Thuc
# Link: https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: 
            return True
        lo = 1
        hi = num/2 + 1
        while lo < hi:
            mid = (lo + hi) / 2
            midsq = mid**2
            if midsq == num:
                return True
            elif midsq < num:
                lo = mid + 1
            else:
                hi = mid

        return False