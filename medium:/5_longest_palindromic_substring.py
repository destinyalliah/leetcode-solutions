# Problem: Longest Palindromic Substring
# Difficulty: Medium
# LeetCode URL: https://leetcode.com/problems/longest-palindromic-substring/
# Solution by: Your Name
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #initialise the longest string
        longest = ""
        #define the pointers as a function
        def pointer(left, right):
            #ensure that the left and right pointers doesn't go outside of the string
            while left >= 0 and right < len(s) and s[left] == s[right]:
                #move pointers left and right
                left -= 1
                right += 1
            #return the characters in the string that are a part of the palindrome
            return s[left + 1:right]

        #loop through the characters in the string
        for i in range(len(s)):
            #test odd palindromes
            p1 = pointer(i, i)
            #test even palindromes
            p2 = pointer(i, i+1)

            #returns the longest palindrome using the even and odd palindrome testing
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
            
        return longest
