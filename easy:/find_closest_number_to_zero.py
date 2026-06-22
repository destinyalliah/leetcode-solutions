class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i 
            else:
                if abs(i) == abs(closest) and i > 0:
                    closest = i
        return closest