class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 == 0:
            x = num // 3
            return [x - 1, x, x + 1]
        return []