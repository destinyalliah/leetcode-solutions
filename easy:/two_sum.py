# Problem: Two Sum
# Difficulty: Easy
# LeetCode URL: https://leetcode.com/problems/two-sum/
# Solution by: Destiny
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Dictionary to store previously seen numbers and their indices
        # Key   -> number from nums
        # Value -> index of that number
        num_map = {}

        # Iterate through the list while keeping track of index and value
        for i, num in enumerate(nums):

            # Calculate the value needed to reach the target
            complement = target - num

            # Check if the complement has already been seen
            if complement in num_map:
                # If found, return the indices of the two numbers
                return [num_map[complement], i]

            # Store the current number and its index for future lookups
            num_map[num] = i
