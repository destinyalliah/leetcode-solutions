class Solution(object):
    def groupAnagrams(self, strs):
        #create a dictionary to make key, value pairs
        groups = {}
        #loop through each word in the list
        for word in strs:
            #needs to be a tuple to be able to be accessed by dictionary
            sorted_word = tuple(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            groups[sorted_word].append(word)
        return list(groups.values())