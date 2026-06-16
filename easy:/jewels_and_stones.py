class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        #hash set is used when we need to know if something exists
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count += 1
        return count