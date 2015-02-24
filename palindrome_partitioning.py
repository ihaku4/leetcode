class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        return self.partition_helper(s)

    def partition_helper(self, s):
        # if len(s) == 1:
        #     return [[s]]
        result = []
        i = 1
        while i <= len(s):
            if self.is_palindrome(s[:i]):
                rest = self.partition_helper(s[i:])
                if len(rest) == 0:
                    result.append([s[:i]])
                for l in rest:
                    subList = [s[:i]]
                    subList.extend(l)
                    result.append(subList)
            i += 1
        return result

    def is_palindrome(self, s):
        head, tail = 0, len(s) - 1
        while head < tail and s[head] == s[tail]:
            head += 1
            tail -= 1
        return head == tail or head == tail + 1
