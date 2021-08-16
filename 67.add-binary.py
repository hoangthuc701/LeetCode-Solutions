# Author: Nguyen Hoang Thuc
# Link: https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b
        result="";
        tmp = 0
        for i in range(len(a)-1,-1, -1):
            num = (int(a[i]) + int(b[i]) + tmp)%2
            tmp = (int(a[i]) + int(b[i]) + tmp)/2
            result = str(num) + result
        if tmp:
            result = "1"+ result
        return result