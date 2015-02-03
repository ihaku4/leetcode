class Solution:
    map = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        26: 'Z',
    }

    # @return a string
    def convertToTitle(self, num):
        title_list = []
        remain = num
        while remain != 0:
            digit = remain % 26
            if digit == 0:
                digit = 26
                remain -= 26
            title_list.append(digit)
            remain = remain / 26
        title_list.reverse()
        title_list = [Solution.map.get(d) for d in title_list]
        print title_list
        return ''.join(title_list)

s = Solution()
print s.convertToTitle(26)
print s.convertToTitle(1)
print s.convertToTitle(27)
print s.convertToTitle(28)
print s.convertToTitle(52)
