class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_string = []
        for i in range(min(len(word1), len(word2))):
            new_string.append(word1[i])
            new_string.append(word2[i])
        new_string += word1[i+1:]
        new_string += word2[i+1:]
        return "".join(new_string)
        