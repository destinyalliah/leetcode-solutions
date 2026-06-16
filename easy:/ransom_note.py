class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #problem is asking if magazine contains all the characters needed to construct ransomNote
        count = {}
        for letter in magazine:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        
        for letter in ransomNote:
            if letter not in count:
                return False
            elif count[letter] == 1:
                del count[letter]
            else:
                count[letter] -= 1
        return True