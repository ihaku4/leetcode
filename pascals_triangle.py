class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        row = []
        n = 1
        while n <= numRows:
            row = self.next_row(row)
            result.append(row)
            n += 1
        return result

    def next_row(self, row):
        row_n = [1] * (len(row) + 1)
        i = 1
        while i < len(row):
            row_n[i] = row[i] + row[i - 1]
            i += 1
        return row_n


s = Solution()
print s.generate(5)
