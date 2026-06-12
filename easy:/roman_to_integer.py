class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary mapping Roman numerals to integers
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        #initialise the total
        #convert the roman numeral input into a string
        sum = 0
        r = str(s)

        #loop through each numeral
        for i in range(len(r)):
            current = d[r[i]]  # get current value using dictionary

            # Check if there is a next character and if subtraction is needed
            if i + 1 < len(r) and current < d[r[i + 1]]:
                total -= current
            else:
                total += current

        return total
                    
                
