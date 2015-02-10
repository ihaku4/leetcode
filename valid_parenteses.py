class Solution:
    map = {
        '(': ')',
        '[': ']',
        '{': '}',
        }

    # @return a boolean
    def isValid(self, s):
        print s
        stack = []
        for c in s:
            if c in self.map:
                stack.append(c)
            elif len(stack) == 0 or not self.map[stack.pop()] == c:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print s.isValid('asdfghjkl;')
    print s.isValid('(asdfghjkl;')
    print s.isValid('(as)dfghjkl;')
    print s.isValid('(as)d[]{}fghjkl;')
    print s.isValid('(as[)d[]{}fghjkl;')
    print s.isValid('([)[]{}')
    print s.isValid('()[]{}')
    print s.isValid('')
