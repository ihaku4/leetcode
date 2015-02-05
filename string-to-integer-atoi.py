# import functools


class Solution:
    INT_MAX = 0x7fffffff
    INT_MIN = -INT_MAX - 1
    INVALID = 0

    map = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        }

    def overflow_check(func):
        # @functools.wraps(func)
        def wrapper(self, str, base=10):
            num = func(self, str, base)
            if num > Solution.INT_MAX:
                return Solution.INT_MAX
            elif num < Solution.INT_MIN:
                return Solution.INT_MIN
            return num
        return wrapper

    def mark_parse(func):
        # @functools.wraps(func)
        def wrapper(self, str, base=10):
            if len(str) == 0:
                return Solution.INVALID
            positive = True
            if str[0] == '-':
                positive = False
                str = str[1:]
            elif str[0] == '+':
                str = str[1:]
            if base:
                num = func(self, str, base)
            else:
                num = func(self, str)
            return num if positive else -num
        return wrapper

    def not_empty(func):
        def wrapper(self, str, base=10):
            str = str.strip()
            if len(str) == 0:
                return Solution.INVALID
            return func(self, str, base)
        return wrapper

    @not_empty
    @overflow_check
    @mark_parse
    def atoi(self, str, base=10):
        return self.parse_integer(str, base=10)

    # @mark_parse
    # @validate
    def parse_integer(self, str, base=10):
        str = str.lstrip('0')
        if len(str) == 0:
            return 0
        num = 0
        for i in str:
            if i not in Solution.map:
                break
            if num > Solution.INT_MAX:
                return num
            num *= base
            num += Solution.map[i]
        return num

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def _test_dot_float_test(self):
        # XXX how to test float equal?
        self.assertEqual(12.34, 12.34)
        self.assertEqual(1*10 + 2 + 3.0/10 + 4.0/100, 12.34)
        self.assertEqual(1.23 * 1e+12, 1.23e+12)
        self.assertEqual(1.23 * 1e-12, 1.23e-12)

        self.assertEqual(-12.34, -12.34)
        self.assertEqual(-1*10 - 2 - 3.0/10 - 4.0/100, -12.34)
        self.assertEqual(-1.23 * 1e+12, -1.23e+12)
        self.assertEqual(-1.23 * 1e-12, -1.23e-12)

        self.assertEqual(+12.34, +12.34)
        self.assertEqual(+1*10 + 2 + 3.0/10 + 4.0/100, +12.34)
        self.assertEqual(+1.23 * 1e+12, +1.23e+12)
        self.assertEqual(+1.23 * 1e-12, +1.23e-12)

    def _test_dot_float(self):
        self.assertEqual(self.s.atoi('12.34'), 12.34)
        self.assertEqual(self.s.atoi('012.34'), 12.34)
        self.assertEqual(self.s.atoi('012.3400'), 12.34)

        self.assertEqual(self.s.atoi('-12.34'), -12.34)
        self.assertEqual(self.s.atoi('-012.34'), -12.34)
        self.assertEqual(self.s.atoi('-012.3400'), -12.34)
        self.assertEqual(self.s.atoi('-012.3400'), -12.34000)

        self.assertEqual(self.s.atoi('+12.34'), +12.34)
        self.assertEqual(self.s.atoi('+012.34'), +12.34)
        self.assertEqual(self.s.atoi('+012.3400'), +12.34)
        self.assertEqual(self.s.atoi('+012.3400'), +12.34000)

    # TODO how to test float?
    def _test_science_notation_float(self):
        # self.assertEqual(self.s.atoi('1.23e12'), 1.23e12)
        # self.assertEqual(self.s.atoi('1.23e+12'), 1.23e+12)
        # print self.s.atoi('1.23e-12'), 1.23e-12
        # print self.s.atoi('1.23e-12') == 1.23e-12
        # self.assertEqual(self.s.atoi('1.23e-12'), 1.23e-12)
        print abs(self.s.atoi('1.23e12') - 1.23e12)
        print self.s.atoi('1.23e12')
        self.assertTrue(abs(self.s.atoi('1.23e12') - 1.23e12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('1.23e+12') - 1.23e+12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('1.23e-12') - 1.23e-12) < 1e-8)

        self.assertTrue(abs(self.s.atoi('-1.23e12') - -1.23e12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('-1.23e+12') - -1.23e+12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('-1.23e-12') - -1.23e-12) < 1e-8)
        self.assertTrue(
            abs(self.s.atoi('+11e530408314') - +11e530408314) < 1e-8)
        print self.s.atoi('12', base=10)
        print self.s.atoi('12.0', base=16)
        print self.s.parse_integer('-F', base=16)

    def _test_hex_int(self):
        self.assertEqual(self.s.atoi('0x12'), 0x12)
        self.assertEqual(self.s.atoi('0x1f'), 0x1f)
        self.assertEqual(self.s.atoi('-0x1f'), -0x1f)
        self.assertEqual(self.s.atoi('0x1fffffff'), 0x1fffffff)
        self.assertEqual(self.s.atoi('-0x1fffffff'), -0x1fffffff)
        self.assertEqual(self.s.atoi('-0x1ffffffa'), -0x1ffffffa)

    def _test_binary_int(self):
        self.assertEqual(self.s.atoi('0b1'), 0b1)
        self.assertEqual(self.s.atoi('0b01'), 0b01)
        self.assertEqual(self.s.atoi('0b11101'), 0b11101)
        self.assertEqual(self.s.atoi('0b111010000'), 0b111010000)
        self.assertEqual(self.s.atoi('-0b1'), -0b1)
        self.assertEqual(self.s.atoi('-0b01'), -0b01)
        self.assertEqual(self.s.atoi('-0b11101'), -0b11101)
        self.assertEqual(self.s.atoi('-0b111010000'), -0b111010000)

    def _test_oct_int(self):
        self.assertEqual(self.s.atoi('01'), 01)
        self.assertEqual(self.s.atoi('001'), 001)
        self.assertEqual(self.s.atoi('011101'), 011101)
        self.assertEqual(self.s.atoi('0111010000'), 0111010000)
        self.assertEqual(self.s.atoi('-01'), -01)
        self.assertEqual(self.s.atoi('-001'), -001)
        self.assertEqual(self.s.atoi('-011101'), -011101)
        self.assertEqual(self.s.atoi('-0111010000'), -0111010000)
        self.assertEqual(self.s.atoi('-0111010700'), -0111010700)

    def test_dec_int(self):
        self.assertEqual(self.s.atoi('1'), 1)
        self.assertEqual(self.s.atoi('1'), 1)
        self.assertEqual(self.s.atoi('11101'), 11101)
        self.assertEqual(self.s.atoi('111010006'), 111010006)
        self.assertEqual(self.s.atoi('-1'), -1)
        self.assertEqual(self.s.atoi('-1'), -1)
        self.assertEqual(self.s.atoi('-11101'), -11101)
        self.assertEqual(self.s.atoi('-111010000'), -111010000)
        self.assertEqual(self.s.atoi('-111009995'), -111009995)

    def test_special_case(self):
        self.assertEqual(self.s.atoi(''), Solution.INVALID)
        self.assertEqual(self.s.atoi('   '), Solution.INVALID)
        self.assertEqual(self.s.atoi(' 123  '), 123)
        self.assertEqual(self.s.atoi('qwer 123  '), Solution.INVALID)
        self.assertEqual(self.s.atoi('  123k23fsd  '), 123)
        # self.assertEqual(self.s.atoi('  12.3k23fsd  '), 12.3)
        self.assertEqual(self.s.atoi('  111k2.3k23fsd  '), 111)
        # self.assertEqual(self.s.atoi('0x7fffffff'), 0x7fffffff)
        # self.assertEqual(self.s.atoi('-0x80000000'), -0x80000000)
        # self.assertEqual(self.s.atoi('0x80000000'), 0x7fffffff)
        # self.assertEqual(self.s.atoi('-0x80000001'), -0x80000000)


unittest.main()
