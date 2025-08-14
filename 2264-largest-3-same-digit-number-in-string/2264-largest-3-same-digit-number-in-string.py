class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for digit in range(9,-1,-1):
            triple=chr(ord('0')+digit)*3
            if triple in num:
                return triple
        return ""