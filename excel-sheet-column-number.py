class Solution:
    map = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
        }

    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0
        size = 1
        for c in s[::-1]:
            num += Solution.map[c] * size
            size *= 26
        return num

s = Solution()
print s.titleToNumber('A')
print s.titleToNumber('Z')
print s.titleToNumber('AA')
print s.titleToNumber('AB')
print s.titleToNumber('AZ')
