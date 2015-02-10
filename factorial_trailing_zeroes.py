class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        n5 = 0
        while n > 0:
            n /= 5
            n5 += n
        return n5


s = Solution()
# print s.trailing_zeros(1234000)(3)
# print s.trailing_zeros(1234000)(4)
# print s.trailing_zeros(1234000)(2)

def fact(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

def count0(n):
    i = 0
    while n % 10 == 0:
        i += 1
        n /= 10
    return i

print fact(100)
print count0(fact(100))
# 100
# 25
#   25 * 2, 25 * 3

# 10 * 10 * 10
# 5 * 5 * 5
print s.trailingZeroes(100)
print '&&&&&&&&&&&&&&&&&&&&&&&&&&&& '
print fact(1000)


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_normal(self):
        print ' dsfaf'
        for i in range(1000):
            self.assertEqual(count0(fact(i)), s.trailingZeroes(i))


unittest.main()



