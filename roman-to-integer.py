class Solution:
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # @return an integer
    def romanToInt(self, s):
        num = 0
        i = 1
        while i < len(s):
            pre = Solution.map[s[i-1]]
            n = Solution.map[s[i]]
            if pre < n:
                num -= pre
            else:
                num += pre
            i += 1
        num += Solution.map[s[-1]]
        return num


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        return

    def test_normal(self):
        self.assertEqual(0, 0)
        self.assertTrue(True)

    def test_data_from_net(self):
        for key in Test.map:
            self.assertEqual(Test.map[key], self.s.romanToInt(key))

    map = {
        'I': 1,
        'XXXII': 32,
        'LXIII': 63,
        'XCIV': 94,
        'II': 2,
        'XXXIII': 33,
        'LXIV': 64,
        'XCV': 95,
        'III': 3,
        'XXXIV': 34,
        'LXV': 65,
        'XCVI': 96,
        'IV': 4,
        'XXXV': 35,
        'LXVI': 66,
        'XCVII': 97,
        'V': 5,
        'XXXVI': 36,
        'LXVII': 67,
        'XCVIII': 98,
        'VI': 6,
        'XXXVII': 37,
        'LXVIII': 68,
        'XCIX': 99,
        'VII': 7,
        'XXXVIII': 38,
        'LXIX': 69,
        'C': 100,
        'VIII': 8,
        'XXXIX': 39,
        'LXX': 70,
        'IX': 9,
        'XL': 40,
        'LXXI': 71,
        'X': 10,
        'XLI': 41,
        'LXXII': 72,
        'DI': 501,
        'XI': 11,
        'XLII': 42,
        'LXXIII': 73,
        'DL': 550,
        'XII': 12,
        'XLIII': 43,
        'LXXIV': 74,
        'DXXX': 530,
        'XIII': 13,
        'XLIV': 44,
        'LXXV': 75,
        'DCCVII': 707,
        'XIV': 14,
        'XLV': 45,
        'LXXVI': 76,
        'DCCCXC': 890,
        'XV': 15,
        'XLVI': 46,
        'LXXVII': 77,
        'MD': 1500,
        'XVI': 16,
        'XLVII': 47,
        'LXXVIII': 78,
        'MDCCC': 1800,
        'XVII': 17,
        'XLVIII': 48,
        'LXXIX': 79,
        'CM': 900,
        'XVIII': 18,
        'XLIX': 49,
        'LXXX': 80,
        'XIX': 19,
        'L': 50,
        'LXXXI': 81,
        'XX': 20,
        'LI': 51,
        'LXXXII': 82,
        'XXI': 21,
        'LII': 52,
        'LXXXIII': 83,
        'XXII': 22,
        'LIII': 53,
        'LXXXIV': 84,
        'XXIII': 23,
        'LIV': 54,
        'LXXXV': 85,
        'XXIV': 24,
        'LV': 55,
        'LXXXVI': 86,
        'XXV': 25,
        'LVI': 56,
        'LXXXVII': 87,
        'XXVI': 26,
        'LVII': 57,
        'LXXXVIII': 88,
        'XXVII': 27,
        'LVIII': 58,
        'LXXXIX': 89,
        'XXVIII': 28,
        'LIX': 59,
        'XC': 90,
        'XXIX': 29,
        'LX': 60,
        'XCI': 91,
        'XXX': 30,
        'LXI': 61,
        'XCII': 92,
        'XXXI': 31,
        'LXII': 62,
        'XCIII': 93,
    }

if __name__ == '__main__':
    unittest.main()
