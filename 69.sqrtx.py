# Author: Nguyen Hoang Thuc
# Link: https://leetcode.com/problems/sqrtx

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        n = x // 2
        left, right = 1, n
        while (left < right):
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                if (mid + 1)*(mid + 1) > x: 
                    return mid
                if left != mid:
                    left = mid
                else:
                    left = mid + 1
            else:
                return mid
        return left
        