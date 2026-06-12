class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #formula for finding the length of a list
        missing_number = (n*(n+1))// 2 - sum(nums)
        return missing_number