# import functools


class Solution:
    INT_MAX = 0x7fffffff
    INT_MIN = -INT_MAX - 1
    INVALID = 0
    map = {}
    for i in '0123456789':
        map[i] = ord(i) - ord('0')
    for i in 'ABCDEF':
        map[i] = ord(i) - ord('A') + 10

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

    def validate(func):
        def wrapper(self, str, base=10):
            not_valid = {
                2: lambda c: c not in '01',
                8: lambda c: c not in '01234567',
                # 10: lambda c: c not in '.0123456789',
                10: lambda c: c not in '0123456789',
                16: lambda c: c not in '0123456789ABCDEF',
                }
            for i in range(len(str)):
                if not_valid[base](str[i]):
                    if i == 0:
                        return Solution.INVALID
                    else:
                        str = str[0:i]
                        break
            return func(self, str, base)
        return wrapper

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
    # @return an integer

    @not_empty
    @overflow_check
    @mark_parse
    def atoi(self, str, base=10):
        num = None
        str = str.upper()
        # if str.count('E') > 0 and not str.startswith('0X'):
        #     pass
        #     num = self.parse_scientific_notation(str)
        # elif str.count('.') > 0:
        #     pass
        #     num = self.parse_dot_float(str)
        # else:
        if str.startswith('0X'):
            num = self.parse_integer(str[2:], base=16)
        elif str.startswith('0B'):
            num = self.parse_integer(str[2:], base=2)
        elif str.startswith('0'):
            num = self.parse_integer(str[1:], base=8)
        else:
            num = self.parse_integer(str, base=10)
        return num

    def parse_scientific_notation(self, str):
        head, tail = str.split('E')
        if head.count('.') > 0:
            num = self.parse_dot_float(head)
        else:
            num = self.parse_integer(head)
        e = self.parse_integer(tail)
        size = 1.0
        if e < 0:
            i = e
            while i < 0:
                size /= 10
                i += 1
        else:
            i = 0
            while i < e:
                size *= 10
                i += 1
        return num * size

    @mark_parse
    @validate
    def parse_integer(self, str, base=10):
        str = str.lstrip('0')
        if len(str) == 0:
            return 0
        num = 0
        size = 1
        for i in str[::-1]:
            if i not in Solution.map:
                break
            num += Solution.map[i] * size
            size *= base
        return num

    @mark_parse
    @validate
    def parse_dot_float(self, str, base=10):
        sp = str.split('.', 1)
        head = sp[0]
        num = self.parse_integer(head)
        if len(sp) == 1:
            return num
        tail = sp[1].rstrip('0')
        if len(tail) == 0:
            return num + 0.0
        size = base * 1.0
        for i in tail:
            if i not in Solution.map:
                break
            num += Solution.map[i] / size
            size *= base
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

    def test_hex_int(self):
        self.assertEqual(self.s.atoi('0x12'), 0x12)
        self.assertEqual(self.s.atoi('0x1f'), 0x1f)
        self.assertEqual(self.s.atoi('-0x1f'), -0x1f)
        self.assertEqual(self.s.atoi('0x1fffffff'), 0x1fffffff)
        self.assertEqual(self.s.atoi('-0x1fffffff'), -0x1fffffff)
        self.assertEqual(self.s.atoi('-0x1ffffffa'), -0x1ffffffa)

    def test_binary_int(self):
        self.assertEqual(self.s.atoi('0b1'), 0b1)
        self.assertEqual(self.s.atoi('0b01'), 0b01)
        self.assertEqual(self.s.atoi('0b11101'), 0b11101)
        self.assertEqual(self.s.atoi('0b111010000'), 0b111010000)
        self.assertEqual(self.s.atoi('-0b1'), -0b1)
        self.assertEqual(self.s.atoi('-0b01'), -0b01)
        self.assertEqual(self.s.atoi('-0b11101'), -0b11101)
        self.assertEqual(self.s.atoi('-0b111010000'), -0b111010000)

    def test_oct_int(self):
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
        self.assertEqual(self.s.atoi('0x7fffffff'), 0x7fffffff)
        self.assertEqual(self.s.atoi('-0x80000000'), -0x80000000)
        self.assertEqual(self.s.atoi('0x80000000'), 0x7fffffff)
        self.assertEqual(self.s.atoi('-0x80000001'), -0x80000000)


unittest.main()
