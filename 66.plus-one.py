# Author: Nguyen Hoang Thuc
# Link: https://leetcode.com/problems/plus-one


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
         
        a = 1
        num = 0
        lens = len(digits)
        for i in range(lens-1, -1, -1):
            num = num + digits[i]*a
            a = a *10
        
        num = num + 1
        
        bytes=int(math.log10(num))
        lens_new=bytes+1
        result=[]
        for i in range(lens_new):
            single=int(num/(10**(bytes-i)))
            result.append(single)
            num=num-single*10**(bytes-i)
        return result
