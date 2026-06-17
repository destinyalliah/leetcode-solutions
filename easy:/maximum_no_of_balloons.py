from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        #use a hashmap as a key, using balloon 
        #if the count is less than 0 then break
        #set a dictionary, if letter in dictionary, add
        
        #the counter import counts every letter in the text in one line, and automatically returns 0 for any character not in text
        count = Counter(text)

        return min (
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n'],
        )

