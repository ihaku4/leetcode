def divide(x, y):
  positive = True
  positive = not positive if x < 0 else positive
  positive = not positive if y < 0 else positive
  res = abs(x) / abs(y)
  return res if positive else -res

class Solution:
  OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    #'/': lambda x, y: x / y,
    '/': divide,
    }

#  PRECEDENCE = {
#    '+': 1,
#    '-': 1,
#    '*': 2,
#    '/': 2,
#    }

  def __init__(self):
    self.operatorStack = None
    self.operandStack = None

#  def calculate(self, nextOperator=None):
#    while (len(self.operatorStack) > 0 and
#           (nextOperator is None or
#            Solution.PRECEDENCE[nextOperator] <= Solution.PRECEDENCE[self.operatorStack[-1]]
#           )
#          ):
  def calculate(self):
    while len(self.operatorStack) > 0:
      operator = self.operatorStack.pop()
      n2, n1 = self.operandStack.pop(), self.operandStack.pop()
      res = Solution.OPERATIONS[operator](n1, n2)
      self.operandStack.append(res)

  # @param {string[]} tokens
  # @return {integer}
  def evalRPN(self, tokens):
    self.operatorStack = []
    self.operandStack = []

    for t in tokens:
      if t in Solution.OPERATIONS.keys():
        self.operatorStack.append(t)
        print self.operatorStack
        print self.operandStack
        self.calculate()
      else:
        self.operandStack.append(int(t))
    print self.operatorStack
    print self.operandStack
    self.calculate()
    return self.operandStack[0]



import unittest

class Test(unittest.TestCase):
  def setUp(self):
    self.s = Solution()
    pass

  def test_default_case(self):
    self.assertEqual(9, self.s.evalRPN(["2", "1", "+", "3", "*"]))
    self.assertEqual(6, self.s.evalRPN(["4", "13", "5", "/", "+"]))
    print '-----------'
    self.assertEqual(22, self.s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    #["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
    #["10","6","   12    ","-11","*","/","*","17","+","5","+"] 
    #["10","6","  -132             ","/","*","17","+","5","+"] 
    #["10","            0              ","*","17","+","5","+"] 
    #["                 0                  ","17","+","5","+"] 
    #["                                       17    ","5","+"] 
    #["                    22                               "] 
if __name__ == '__main__':
  unittest.main()
