class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #empty list for the answer
        ans = []
        #set index i to 0
        i = 0

        #while the index is less than the length of the nums
        while i < len(nums):
            #make the start number the first number in list
            start = nums[i]
            #while i is less than the length of the list and the next number is equal to the current number plus one
            while i < len(nums) - 1 and nums[i] + 1 == nums [i+1]:
                #increase i by one
                    i +=1
                
                #if the first value is not equal to the current value
            if start != nums[i]:
                    #return the range
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))
                
            i += 1

        return ans