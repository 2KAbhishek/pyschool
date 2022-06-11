from person import Person
from student import Student


class Staff(Person):
    """
    >>> C = Catalog()
    >>> C._loadCatalog("../data/catalog.csv")
    >>> s1 = Staff('Jane Doe', '214-49-2890')
    >>> s1.getSupervisor
    >>> s2 = Staff('John Doe', '614-49-6590', s1)
    >>> s2.getSupervisor
    Staff(Jane Doe, 905jd2890)
    >>> s1 == s2
    False
    >>> s2.id
    '905jd6590'
    >>> p = Person('Jason Smith', '221-11-2629')
    >>> st1 = s1.createStudent(p)
    >>> isinstance(st1, Student)
    True
    >>> s2.applyHold(st1)
    'Completed!'
    >>> st1.registerSemester()
    'Unsuccessful operation'
    >>> s2.removeHold(st1)
    'Completed!'
    >>> st1.registerSemester()
    >>> st1.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> st1.semesters
    {1: CMPSC 132}
    >>> s1.applyHold(st1)
    'Completed!'
    >>> st1.enrollCourse('CMPSC 360', C)
    'Unsuccessful operation'
    >>> st1.semesters
    {1: CMPSC 132}
    """

    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name, ssn)
        self.supervisor = supervisor

    def __str__(self):
        return "Staff(" + self.name + ", " + self.id + ")"

    __repr__ = __str__

    @property
    def id(self):
        name_words = self.name.split(" ")
        initials = ""
        for word in name_words:
            initials += word[0]
        return "905" + initials.lower() + self.ssn[-4:]

    @property
    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        self.supervisor = new_supervisor

    def applyHold(self, student):
        """Add a student from the hold of the staff
        Args:
            student (Student): Student to be unenrolled
        Returns:
            str: Success message
        """
        if student.hold == None:
            student.hold = self
            return "Completed!"

    def removeHold(self, student):
        """Remove a student from the hold of the staff
        Args:
            student (Student): Student to be unenrolled
        Returns:
            str: Success message
        """
        if student.hold == self:
            student.hold = None
            return "Completed!"

    def unenrollStudent(self, student):
        """Marks a student as unenrolled
        Args:
            student (Student): Student to be unenrolled
        Returns:
            str: Success message
        """
        student.active = False
        return "Completed!"

    def createStudent(self, person):
        """Creates a student object
        Args:
            person (Person): Person object
        Returns:
            Student: New Student Object
        """
        return Student(person.name, person.ssn, "Freshman")


if __name__ == "__main__":
    import doctest
    from catalog import Catalog
    from course import Course

    doctest.testmod()
