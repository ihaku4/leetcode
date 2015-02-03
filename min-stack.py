class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        self.min_value = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min) == 0 or \
           self.stack[self.min[-1]] > x:
            self.min.append(len(self.stack) - 1)
            self.min_value = x
        return x

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return
        self.stack.pop()
        if self.min[-1] == len(self.stack):
            self.min.pop()
            if len(self.min) == 0:
                self.min_value = None
            else:
                self.min_value = self.stack[self.min[-1]]

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.min_value


def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
            continue
        elif arr[mid] > target:
            end = mid - 1
            continue
    return -1


def binary_insert(arr, target):
    if len(arr) == 0:
        return 0
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
            continue
        elif arr[mid] > target:
            end = mid - 1
            continue
    return start


def quickSort(lst):
    # List of 0 or 1 items is already sorted
    if len(lst) <= 1:
        return lst
    else:
        # Pivot can be chosen randomly
        # pivotIndex = randint(0, len(lst)-1)
        pivotIndex = 0
        pivot = lst[pivotIndex]
        # Elements lower than and greater than pivot
        lesser, greater = [], []

        for index in range(len(lst)):
            # Don't do anything if you're at the pivot
            if index == pivotIndex:
                pass
            else:
                # Sort elements into < pivot and >= pivot
                el = lst[index]
                if el < pivot:
                    lesser.append(el)
                else:
                    greater.append(el)

        # Sort lesser and greater, concatenate results
        return quickSort(lesser) + [pivot] + quickSort(greater)


s = MinStack()
for i in range(-10000, 0):
    s.push(i)
print s.getMin()

print binary_search([1, 3, 5, 7, 49, 100], 4)
print binary_insert([1, 3, 5, 7, 49, 100], 6)
