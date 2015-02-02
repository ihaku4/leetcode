class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if self.isBegin(c):
                stack.append(c)
            elif self.isEnd(c) and \
                    (len(stack) == 0 or not self.match(stack.pop(), c)):
                return False
        return len(stack) == 0

    def isBegin(self, c):
        return c in '([{'

    def isEnd(self, c):
        return c in ')]}'

    def match(self, begin, end):
        return begin == '(' and end == ')' or \
            begin == '[' and end == ']' or \
            begin == '{' and end == '}'


if __name__ == '__main__':
    s = Solution()
    print s.isValid('asdfghjkl;')
    print s.isValid('(asdfghjkl;')
    print s.isValid('(as)dfghjkl;')
    print s.isValid('(as)d[]{}fghjkl;')
    print s.isValid('(as[)d[]{}fghjkl;')
