class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        ia = ib = 0
        while ia < m + ib and ib < n:
            ia = self.binary_search(A, ia, m + ib - 1, B[ib])
            if ia >= m + ib:
                break

            off = 1
            while ib + off < n and A[ia] > B[ib + off]:
                off = off + 1

            self.shift(A, m + ib, ia, off)
            for i in range(off):
                A[ia + i] = B[ib + i]

            ia = ia + off
            ib = ib + off
        if ib < n:
            for i in range(n - ib):
                A[ia + i] = B[i + ib]

    def binary_search(self, arr, start, end, target):
        while start <= end:
            mid = (start + end) / 2
            if mid == start:
                if target <= arr[start]:
                    return start
                elif target > arr[start] and target <= arr[end]:
                    return start + 1
                elif target > arr[end]:
                    return end + 1

            if arr[mid] <= target and arr[mid + 1] > target:
                return mid + 1
            elif arr[mid] <= target and arr[mid + 1] <= target:
                start = mid + 1
                continue
            elif arr[mid] > target and arr[mid + 1] > target:
                end = mid
                continue

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
