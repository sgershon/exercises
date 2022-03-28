"""
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # TODO: Switch: Check for double letters first

        sum = 0
        skip = False
        for i, l in enumerate(s):
            if skip:
                skip = False
                continue
            if l == 'M': sum += 1000
            if l == 'D': sum += 500
            if l == 'C':
                if i+1 < len(s):
                    if s[i+1] == 'D':
                        sum += 400  # We add another 1...
                        skip = True
                    elif s[i+1] == 'M':
                        sum += 900  # We add another 1...
                        skip = True
                    else:
                        sum += 100
                else:
                    sum += 100
            if l == 'L': sum += 50
            if l == 'X':
                if i+1 < len(s):
                    if s[i+1] == 'L':
                        sum += 40  # We add another 1...
                        skip = True
                    elif s[i+1] == 'C':
                        sum += 90  # We add another 1...
                        skip = True
                    else:
                        sum += 10
                else:
                    sum += 10
            if l == 'V': sum += 5
            if l == 'I':
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        sum += 4  # We add another 1...
                        skip = True
                    elif s[i+1] == 'X':
                        sum += 9  # We add another 1...
                        skip = True
                    else:
                        sum += 1
                else:
                    sum += 1
        return sum

s = Solution()
print(s.romanToInt("MCMXCIV"))
