from course import Course


class Catalog:
    """
    >>> C = Catalog()
    >>> C.courseOfferings
    {}
    >>> C._loadCatalog("../data/catalog.csv")
    >>> C.courseOfferings
    {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
    >>> C.removeCourse('CMPSC 360')
    'Course removed successfully'
    >>> C.courseOfferings
    {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
    >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
    True
    """

    def __init__(self):
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        """Add a course to the catalog.

        Args:
            cid (str): course id
            cname (str): course name
            credits (int): number of credits
        """
        if cid in self.courseOfferings:
            return "Course already added"
        else:
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return "Course added successfully"

    def removeCourse(self, cid):
        """Remove a course from the catalog.

        Args:
            cid (str): course id
        """
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        else:
            return "Course not found"

    def _loadCatalog(self, file):
        """Load a catalog from a file.
        Args:
            file (str): file path
        """
        with open(file, "r") as f:
            course_info = f.read()
            course_info = course_info.split("\n")
            for course in course_info:
                course = course.split(",")
                self.addCourse(course[0], course[1], int(course[2])) if len(
                    course
                ) == 3 else None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
