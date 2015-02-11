class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if min(len(a), len(b)) == 0:
            return ''
        longDig, shortDig = (b, a) if len(b) > len(a) else (a, b)
        result = ['0'] * (len(longDig) + 1)
        iS = len(shortDig) - 1
        iL = len(longDig) - 1
        iRe = len(result) - 1
        advance = False
        while iS >= 0:
            count = 1 if advance else 0
            if longDig[iL] == '1' and shortDig[iS] == '1':
                count += 2
            elif longDig[iL] == '1' or shortDig[iS] == '1':
                count += 1

            advance = True if count > 1 else False
            if count % 2 == 1:
                result[iRe] = '1'
            iS -= 1
            iL -= 1
            iRe -= 1
        while iL >= 0:
            count = 1 if advance else 0
            if longDig[iL] == '1':
                count += 1
            advance = True if count > 1 else False
            if count % 2 == 1:
                result[iRe] = '1'
            iL -= 1
            iRe -= 1
        if advance:
            result[iRe] = '1'
        else:
            result = result[1:]
        return ''.join(result)


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual('100', self.s.addBinary('11', '1'))
        self.assertEqual('1000', self.s.addBinary('111', '1'))
        self.assertEqual('1010', self.s.addBinary('1000', '10'))
        self.assertEqual('0', self.s.addBinary('0', '0'))
        self.assertEqual('10', self.s.addBinary('1', '1'))
        self.assertEqual('10101', self.s.addBinary('1010', '1011'))

if __name__ == '__main__':
    unittest.main()
