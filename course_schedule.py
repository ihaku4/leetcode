class Course:
    def __init__(self, n):
        self.n = n
        self.dependences = []

class Solution:

    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        courses = [Course(n) for n in xrange(numCourses)]
        for p in prerequisites:
            c1, c2 = p
            courses[c1].dependences.append(courses[c2]) 

        finished = set()
        workingOn = set()
        for c in courses:
            if not self.studyCourse(c, finished, workingOn):
                return False
        return True

    def studyCourse(self, course, finished, workingOn):
        if course in finished:  return True
        if course in workingOn: return False

        workingOn.add(course)
        for d in course.dependences:
            if not self.studyCourse(d, finished, workingOn):
                return False
        finished.add(course)
        workingOn.remove(course)
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
