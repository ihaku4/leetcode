import functools


class Solution:
    map = {}
    for i in '0123456789':
        map[i] = ord(i) - ord('0')
    for i in 'ABCDEF':
        map[i] = ord(i) - ord('A') + 10

    def mark_parse(func):
        @functools.wraps(func)
        def wrapper(self, str, base=10):
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

    @mark_parse
    def atoi(self, str, base=10):
        # validate TODO

        num = None
        str = str.upper()
        if str.count('E') > 0 and not str.startswith('0X'):
            num = self.parse_scientific_notation(str)
        elif str.count('.') > 0:
            num = self.parse_dot_float(str)
        elif str.startswith('0X'):
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
            for i in range(e, 0):
                size /= 10
        else:
            for i in range(e):
                size *= 10
        return num * size

    @mark_parse
    def parse_integer(self, str, base=10):
        str = str.lstrip('0')
        if len(str) == 0:
            return 0
        num = 0
        size = 1
        for i in str[::-1]:
            num += Solution.map[i] * size
            size *= base
        return num

    @mark_parse
    def parse_dot_float(self, str, base=10):
        head, tail = str.split('.')
        num = self.parse_integer(head)
        tail = tail.rstrip('0')
        if len(tail) == 0:
            return num + 0.0
        size = base * 1.0
        for i in tail:
            num += Solution.map[i] / size
            size *= base
        return num

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

        self.assertEqual(-12.34, -12.34)
        self.assertEqual(-1*10 - 2 - 3.0/10 - 4.0/100, -12.34)
        self.assertEqual(-1.23 * 1e+12, -1.23e+12)
        self.assertEqual(-1.23 * 1e-12, -1.23e-12)

        self.assertEqual(+12.34, +12.34)
        self.assertEqual(+1*10 + 2 + 3.0/10 + 4.0/100, +12.34)
        self.assertEqual(+1.23 * 1e+12, +1.23e+12)
        self.assertEqual(+1.23 * 1e-12, +1.23e-12)

    def test_dot_float(self):
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
    def test_science_notation_float(self):
        # self.assertEqual(self.s.atoi('1.23e12'), 1.23e12)
        # self.assertEqual(self.s.atoi('1.23e+12'), 1.23e+12)
        # print self.s.atoi('1.23e-12'), 1.23e-12
        # print self.s.atoi('1.23e-12') == 1.23e-12
        # self.assertEqual(self.s.atoi('1.23e-12'), 1.23e-12)
        self.assertTrue(abs(self.s.atoi('1.23e12') - 1.23e12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('1.23e+12') - 1.23e+12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('1.23e-12') - 1.23e-12) < 1e-8)

        self.assertTrue(abs(self.s.atoi('-1.23e12') - -1.23e12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('-1.23e+12') - -1.23e+12) < 1e-8)
        self.assertTrue(abs(self.s.atoi('-1.23e-12') - -1.23e-12) < 1e-8)
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

unittest.main()
