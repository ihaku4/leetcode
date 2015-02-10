class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1] * (rowIndex + 1)
        n = 1
        while n <= rowIndex:
            self.next_row(result, n)
            n += 1
        return result

    def next_row(self, row, rowIndex):
        i = 1
        pre = row[i - 1]
        while i < rowIndex:
            current = row[i]
            row[i] += pre
            pre = current
            i += 1
        row[i] = 1


s = Solution()
print s.getRow(0)
print s.getRow(1)
print s.getRow(2)
print s.getRow(3)
print s.getRow(4)
print s.getRow(5)
print s.getRow(6)
print s.getRow(7)
print s.getRow(8)
print s.getRow(9)
print s.getRow(10)
print s.getRow(11)
