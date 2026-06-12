class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count = {}
        
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        sorted_nums = sorted(num_count, key = lambda x:num_count[x], reverse = True)
        #the [:k] slice takes just the first k elements
        return sorted_nums[:k]