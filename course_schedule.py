class Course:
    def __init__(self, n):
        self.n = n
        self.dependences = []
        self.finished = False
        self.workingOn = False

class Solution:

    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        courses = [Course(n) for n in xrange(numCourses)]
        for p in prerequisites:
            c1, c2 = p
            courses[c1].dependences.append(courses[c2]) 

        for c in courses:
            if not self.studyCourse(c):
                return False
        return True

    def studyCourse(self, course):
        if course.finished:     return True
        if course.workingOn:    return False

        course.workingOn = True
        for d in course.dependences:
            if not self.studyCourse(d):
                return False
        course.finished = True
        course.workingOn = False
        return True


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, self.s.canFinish(2, [[1, 0]]))
        self.assertEqual(False, self.s.canFinish(2, [[1, 0], [0, 1]]))
        self.assertEqual(True, self.s.canFinish(3, [[0,1],[0,2],[1,2]]))

if __name__ == '__main__':
    unittest.main()
