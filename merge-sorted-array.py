class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        ia = ib = 0
        while ia < m and ib < n:
            if A[ia + ib] <= B[ib]:
                ia = ia + 1
                continue
            else:
                off = 1
                while ib + off < n and A[ia + ib] > B[ib + off]:
                    off = off + 1
                self.shift(A, m + ib, ia + ib, off)
                for i in range(off):
                    A[ia + ib + i] = B[ib + i]
                ib = ib + off
        if ib < n:
            for i in range(ib, n):
                A[ia + i] = B[i]

    def shift(self, arr, length, start, off=1):
        r = range(start, length)
        r.reverse()
        for i in r:
            arr[i + off] = arr[i]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 4, 0, 0, 0]
    s.shift(arr, 4, 1, 2)
    arr = [1, 2, 3, 4, 0, 0, 0]
    s.shift(arr, 4, 1)
    print arr

    A = [1, 2, 8, 9]
    B = [1, 4, 5, 6, 10, 11]
    A.extend([0, 0, 0, 0, 0, 0])
    print A, B
    s.merge(A, 4, B, 6)
    print A, B
    A = [1, 2, 3]
    B = [2, 5, 6]
    A.extend([0, 0, 0])
    print A, B
    s.merge(A, 3, B, 3)
    print A, B
