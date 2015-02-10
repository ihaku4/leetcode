class Solution:
    # @return an integer
    def reverse(self, x):
        negative = False
        if x < 0:
            x = -x
            negative = True
        re = 0
        while x != 0:
            re *= 10
            re += x % 10
            x = x / 10
        if re > 0x7fffffff and not negative:
            return 0
        if re > 0x80000000 and negative:
            return 0
        return re if not negative else -re


s = Solution()
print 1 / 10
print -1 / 10
print s.reverse(123)
print s.reverse(100)
print s.reverse(-123)
print s.reverse(1000000003)
print s.reverse(-1000000003)
print s.reverse(0x7fffffff)
print
print 0xffffffff
print 0x7fffffff
print 0x80000000
print 1000000003
