from loan import Loan
from student_account import StudentAccount
from person import Person
from semester import Semester


class Student(Person):
    """
    >>> C = Catalog()
    >>> C._loadCatalog("../data/catalog.csv")
    >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    >>> s1
    Student(Jason Lee, jl2890, Freshman)
    >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
    >>> s2
    Student(Karen Lee, kl2670, Freshman)
    >>> s1 == s2
    False
    >>> s1.id
    'jl2890'
    >>> s2.id
    'kl2670'
    >>> s1.registerSemester()
    >>> s1.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> s1.semesters
    {1: CMPSC 132}
    >>> s1.enrollCourse('CMPSC 360', C)
    'Course added successfully'
    >>> s1.enrollCourse('CMPSC 465', C)
    'Course not found'
    >>> s1.semesters
    {1: CMPSC 132; CMPSC 360}
    >>> s2.semesters
    {}
    >>> s1.enrollCourse('CMPSC 132', C)
    'Course already enrolled'
    >>> s1.dropCourse('CMPSC 360')
    'Course dropped successfully'
    >>> s1.dropCourse('CMPSC 360')
    'Course not found'
    >>> s1.semesters
    {1: CMPSC 132}
    >>> s1.registerSemester()
    >>> s1.semesters
    {1: CMPSC 132, 2: No courses}
    >>> s1.enrollCourse('CMPSC 360', C)
    'Course added successfully'
    >>> s1.semesters
    {1: CMPSC 132, 2: CMPSC 360}
    >>> s1.registerSemester()
    >>> s1.semesters
    {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
    >>> s1
    Student(Jason Lee, jl2890, Sophomore)
    """

    failure = "Unsuccessful operation"

    def __init__(self, name, ssn, year):
        super().__init__(name, ssn)
        self.year = year
        self.hold = None
        self.active = True
        self.semesters = {}
        self.account = self.__createStudentAccount()

    def __str__(self):
        return "Student(" + self.name + ", " + self.id + ", " + self.year + ")"

    __repr__ = __str__

    def __createStudentAccount(self):
        return StudentAccount(self)

    @property
    def id(self):
        name_words = self.name.split(" ")
        initials = ""
        for word in name_words:
            initials += word[0]
        return initials.lower() + self.ssn[-4:]

    def registerSemester(self):
        """Register a new semester for the student

        Returns:
            str: Failure message
        """
        if self.active == False or self.hold != None:
            return self.failure

        self.semesters[len(self.semesters) + 1] = Semester()

        if len(self.semesters) >= 6:
            self.year = "Senior"
        elif len(self.semesters) >= 4:
            self.year = "Junior"
        elif len(self.semesters) >= 2:
            self.year = "Sophomore"
        else:
            self.year = "Freshman"

    def enrollCourse(self, cid, catalog):
        """Add a course to the semester
        Args:
            cid (str): Course ID
            catalog (Catalog): Course catalog
        Returns:
            str: Success or failure message
        """
        if cid not in catalog.courseOfferings:
            return "Course not found"

        if cid in self.semesters[max(self.semesters.keys())].courses:
            return "Course already enrolled"

        if self.active == False or self.hold != None:
            return self.failure

        self.semesters[max(self.semesters.keys())].courses[
            cid
        ] = catalog.courseOfferings[cid]

        self.account.chargeAccount(
            catalog.courseOfferings[cid].credits * self.account.CREDIT_PRICE
        )
        return "Course added successfully"

    def dropCourse(self, cid):
        """Drops a course from semester
        Args:
            cid (str): Course ID
        Returns:
            str: Success or failure message
        """
        if self.active == False or self.hold != None:
            return self.failure

        if cid not in self.semesters[max(self.semesters.keys())].courses:
            return "Course not found"

        self.account.makePayment(
            (
                self.semesters[max(self.semesters.keys())].courses[cid].credits
                * self.account.CREDIT_PRICE
            )
            / 2
        )
        del self.semesters[max(self.semesters.keys())].courses[cid]
        return "Course dropped successfully"

    def getLoan(self, amount):
        """Get a loan for the student
        Args:
            amount (float): Amount of loan
        Returns:
            str: Failure message
        """
        if self.active == False:
            return self.failure

        if not self.semesters[max(self.semesters.keys())].isFullTime:
            return "Not full-time"

        loan = Loan(amount)
        self.account.loans[loan.loan_id] = loan
        self.account.makePayment(amount)


if __name__ == "__main__":
    import doctest

    from catalog import Catalog
    from course import Course

    doctest.testmod()
