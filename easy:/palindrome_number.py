class Solution(object):
    #define the function based of the integer
    def isPalindrome(self, x):
        #if the number is a negative number, return false
        if x < 0:
            return False
        
        #convert the integer x into as string
        s = str(x)
        #this is called multiple assignment
        #left = 0
        #right = len(s) - 1
        left, right = 0, len(s) - 1

        #create a while loop to run to compare all of numbers in the integer
        while left < right:
            #return false if the left side is not equal to the right side
            if s[left] != s[right]:
                return False
            #keep comparing all the numbers in the integer
            left += 1
            right -= 1
        #return true if false is never returned
        return True