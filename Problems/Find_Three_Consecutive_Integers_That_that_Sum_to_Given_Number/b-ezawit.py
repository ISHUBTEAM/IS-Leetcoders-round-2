class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if(num%3 !=0):
            return []
        else:
            x = (num - 3)/3
            return [x,x+1,x+2]