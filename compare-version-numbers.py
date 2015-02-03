class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        ver1Split = version1.split('.')
        ver2Split = version2.split('.')
        p = 0
        headResult = self.compareSubVersion(ver1Split[p], ver2Split[p])
        headResult = 0
        while headResult == 0:
            headResult = self.compareSubVersion(ver1Split[p], ver2Split[p])
            if headResult != 0:
                return headResult
            p += 1
            if len(ver1Split) < p + 1 and len(ver2Split) < p + 1:
                return 0
            elif len(ver1Split) < p + 1 and len(ver2Split) >= p + 1:
                if self.isZero(ver2Split[p:]):
                    return 0
                return -1
            elif len(ver1Split) >= p + 1 and len(ver2Split) < p + 1:
                if self.isZero(ver1Split[p:]):
                    return 0
                return 1

    def isZero(self, versionArray):
        for v in versionArray:
            if self.removePreZeros(v) != '':
                return False
        return True

    def compareSubVersion(self, str1, str2):
        str1 = self.removePreZeros(str1)
        str2 = self.removePreZeros(str2)
        if len(str1) > len(str2):
            return 1
        elif len(str1) < len(str2):
            return -1
        else:
            for i in range(len(str1)):
                if ord(str1[i]) > ord(str2[i]):
                    return 1
                elif ord(str1[i]) < ord(str2[i]):
                    return -1
            return 0

    def removePreZeros(self, string):
        i = 0
        while i < len(string) and string[i] == '0':
            i += 1
        return string[i:]

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_version(self):

        self.assertEqual(-1, self.s.compareVersion('1.2', '1.3'))
        self.assertEqual( 1, self.s.compareVersion('1.4', '1.3'))
        self.assertEqual( 1, self.s.compareVersion('2.3', '1.3'))
        self.assertEqual(-1, self.s.compareVersion('2.3', '3.2'))
        self.assertEqual( 1, self.s.compareVersion('1', '0'))
        self.assertEqual( 0, self.s.compareVersion('1', '1'))
        self.assertEqual( 0, self.s.compareVersion('01', '1'))
        self.assertEqual( 1, self.s.compareVersion('0.1', '0.0.1'))
        self.assertEqual( 0, self.s.compareVersion('1.0', '1'))

unittest.main()
