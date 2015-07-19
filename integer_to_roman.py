class Solution:
    itor = {
        1:      'I',
        5:      'V',
        10:     'X',
        50:     'L',
        100:    'C',
        500:    'D',
        1000:   'M',
    }

    basicForm = {
        1:  [1],
        2:  [1, 1],
        3:  [1, 1, 1],
        4:  [1, 5],
        5:  [5],
        6:  [5, 1],
        7:  [5, 1, 1],
        8:  [5, 1, 1, 1],
        9:  [1, 10],
        10: [10],
        0:  [],
    }

    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        roman = ''
        n = 1
        while num / n > 0:
            digit = num / n % 10
            form = Solution.basicForm[digit]
            roman = ''.join([Solution.itor[x * n] for x in form]) + roman
            n *= 10
        return roman


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual('XCIX', self.s.intToRoman(99))
        self.assertEqual('LXXX', self.s.intToRoman(80))
        self.assertEqual('LXXXVIII', self.s.intToRoman(88))

if __name__ == '__main__':
    unittest.main()
