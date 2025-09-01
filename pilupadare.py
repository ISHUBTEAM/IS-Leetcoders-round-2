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
        return value
 
def finalValueAfterOperations(operations):
    value = 0
    for operation in operations:
        if operation in ("++X", "X++"):
            value += 1
        else:
            value -= 1
    return value
