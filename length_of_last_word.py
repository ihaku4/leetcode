class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end >= 0 and s[end] == ' ':
            end -= 1
        lenLast = 0
        while end >= 0 and s[end] != ' ':
            lenLast += 1
            end -= 1
        return lenLast


s = Solution()
print s.lengthOfLastWord('Hello World')
print s.lengthOfLastWord('Hello World   ')
print s.lengthOfLastWord('     Hello   World   ')
