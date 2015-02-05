class Solution:
    # @return an integer
    def atoi(self, str):
        # integer literal types:
        #
        #   1. 0xffff, 0Xffff, 0xFFFF, 0XFFFF, 0xffFf, 0x000f
        #   2. 0777, 000777
        #   3. 999
        #   4. 999.12, 1.0
        #   5. 0.12, 0000.12, 00001.12
        #   6. 0b1110, 0B1100, 0b000001
        #   7. 2E12 ?, 2e+12, 2e-12
        #   8. 0F, 0f, 0U, 0u, 0L, 0UL, 0LL

        # 2. upper / lower case
        # 1. base: 0x, 0b, 0, decimal
        # 4. science notation: 1.23e+12
        # 3. trim head 0s, tail 0s

        # validate TODO

        # float: only decimal allowed
        if str.count('.') > 0:
            pass

        # integer
        str = str.upper()
        if str.startswith('0X'):
            pass
        elif str.startswith('0B'):
            pass
        elif str.startswith('0'):
            pass
        else:
            # float: only decimal allowed
            if str.count('E') > 0:
                pass
            else:
                pass

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_dot_float_test(self):
        # XXX how to test float equal?
        self.assertEqual(12.34, 12.34)
        self.assertEqual(1*10 + 2 + 3.0/10 + 4.0/100, 12.34)
        self.assertEqual(1.23 * 1e+12, 1.23e+12)
        self.assertEqual(1.23 * 1e-12, 1.23e-12)

    def _test_dot_float(self):
        self.assertEqual(12.34, 12.34)
        self.assertEqual(1*10 + 2 + 3.0/10 + 4.0/100, 12.34)
        self.assertEqual(self.s.atoi('12.34'), 12.34)
        self.assertEqual(self.s.atoi('012.34'), 12.34)

unittest.main()
