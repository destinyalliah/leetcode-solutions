class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #initialise the pointers
        left, right = 0, len(nums) - 1
        #while the left pointer is less than or same as the right pointer
        while left <= right:
            #find the middle index value
            mid = (left+right)//2
            #if the middle number is equal to the target number
            if nums[mid] == target:
                #return the index of target number
                return mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1
        return -1

