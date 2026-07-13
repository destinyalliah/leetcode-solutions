class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #initialise left and right pointers
        left, right = 1, num
        while left <= right:
            mid = (left+right) // 2
            m_squared = mid * mid
            if m_squared == num:
                return True
            elif m_squared > num:
                right = mid - 1
            else:
                left = mid + 1
        return False