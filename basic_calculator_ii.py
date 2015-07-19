class Solution:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        numberStk = []
        operatorStk = []

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                h = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[h:i])
                numberStk.append(num)
            elif s[i] in '+-*/':
                # calculate pre if possible
                #if len(operatorStk) > 0 and self.canCalculate(operatorStk[-1], s[i]):
                while len(operatorStk) > 0 and self.canCalculate(operatorStk[-1], s[i]):
                    self.processCalculationStack(operatorStk, numberStk)
                operatorStk.append(s[i])
                i += 1

        # calculate the remaining.
        while len(operatorStk) > 0:
            self.processCalculationStack(operatorStk, numberStk)
        return numberStk[0]

    def processCalculationStack(self, operatorStk, numberStk):
        if len(operatorStk) == 0:
            return
        n2 = numberStk.pop()
        n1 = numberStk.pop()
        operator = operatorStk.pop()
        result = Solution.operations[operator](n1, n2)
        numberStk.append(result)
        #print '%d %s %d = %d' % (n1, operator, n2, result)

    def canCalculate(self, operator, operatorAfter):
        return (operator in '*/' or operatorAfter in '+-')


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(17, self.s.calculate('1 + 2 + 3 * 4 + 5 / 2'))
        self.assertEqual(4, self.s.calculate('1 + 2 + 3 * 4 + 5 / 2 - 13'))
        self.assertEqual(-24, self.s.calculate("1*2-3/4+5*6-7*8+9/10"))
        #                                        2 - 0 + 30-56 + 0  = -24

if __name__ == '__main__':
    unittest.main()
