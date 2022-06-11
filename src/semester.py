class Semester:
    """
    >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
    >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
    >>> math230 = Course("MATH 230", 'Calculus', 4)
    >>> phys213 = Course("PHYS 213", 'General Physics', 2)
    >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
    >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
    >>> spr22 = Semester()
    >>> spr22
    No courses
    >>> spr22.addCourse(cmpsc132)
    >>> isinstance(spr22.courses['CMPSC 132'], Course)
    True
    >>> spr22.addCourse(math230)
    >>> spr22
    CMPSC 132; MATH 230
    >>> spr22.isFullTime
    False
    >>> spr22.totalCredits
    7
    >>> spr22.addCourse(phys213)
    >>> spr22.addCourse(econ102)
    >>> spr22.addCourse(econ102)
    'Course already added'
    >>> spr22.addCourse(phil119)
    >>> spr22.isFullTime
    True
    >>> spr22.dropCourse(phil119)
    >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
    >>> spr22.totalCredits
    16
    >>> spr22.dropCourse(cmpsc131)
    'No such course'
    >>> spr22.courses
    {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    """

    def __init__(self):
        self.courses = {}

    def __str__(self):
        if self.courses == {}:
            return "No courses"
        else:
            return "; ".join(self.courses.keys())

    __repr__ = __str__

    def addCourse(self, course):
        """Add a course to the semester.
        Args:
            course (Course): course to drop
        Returns:
            str: Feedback message
        """
        if course.cid in self.courses:
            return "Course already added"
        else:
            self.courses[course.cid] = course

    def dropCourse(self, course):
        """Drop a course from the semester.
        Args:
            course (Course): course to drop
        Returns:
            str: Feedback message
        """
        if course.cid not in self.courses:
            return "No such course"
        else:
            del self.courses[course.cid]

    @property
    def totalCredits(self):
        return sum(course.credits for course in self.courses.values())

    @property
    def isFullTime(self):
        return self.totalCredits >= 12


if __name__ == "__main__":
    import doctest
    from course import Course

    doctest.testmod()
