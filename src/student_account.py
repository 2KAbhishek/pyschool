class StudentAccount:
    """
    >>> C = Catalog()
    >>> C._loadCatalog("../data/catalog.csv")
    >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    >>> s1.registerSemester()
    >>> s1.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> s1.account.balance
    3000
    >>> s1.enrollCourse('CMPSC 360', C)
    'Course added successfully'
    >>> s1.account.balance
    6000
    >>> s1.enrollCourse('MATH 230', C)
    'Course added successfully'
    >>> s1.enrollCourse('PHYS 213', C)
    'Course added successfully'
    >>> print(s1.account)
    Name: Jason Lee
    ID: jl2890
    Balance: $12000
    >>> s1.account.chargeAccount(100)
    12100
    >>> s1.account.balance
    12100
    >>> s1.account.makePayment(200)
    11900
    >>> s1.getLoan(4000)
    >>> s1.account.balance
    7900
    >>> s1.getLoan(8000)
    >>> s1.account.balance
    -100
    >>> s1.enrollCourse('CMPEN 270', C)
    'Course added successfully'
    >>> s1.account.balance
    3900
    >>> s1.dropCourse('CMPEN 270')
    'Course dropped successfully'
    >>> s1.account.balance
    1900.0
    >>> s1.account.loans
    {17412: Balance: $4000, 22004: Balance: $8000}
    >>> StudentAccount.CREDIT_PRICE = 1500
    >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
    >>> s2.registerSemester()
    >>> s2.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> s2.account.balance
    3000
    >>> s1.enrollCourse('CMPEN 270', C)
    'Course added successfully'
    >>> s1.account.balance
    5900.0
    """

    CREDIT_PRICE = 1000

    def __init__(self, student):
        self.student = student
        self.loans = {}
        self.balance = 0

    def __str__(self):
        return (
            "Name: "
            + self.student.name
            + "\n"
            + "ID: "
            + self.student.id
            + "\n"
            + "Balance: $"
            + str(self.balance)
        )

    __repr__ = __str__

    def makePayment(self, amount):
        """Make payment from account
        Args:
            amount (float): Amount to pay
        Returns:
            float: Current balance
        """
        self.balance -= amount
        return self.balance

    def chargeAccount(self, amount):
        """Charge account with amount
        Args:
            amount (float): Amount to charge
        Returns:
            float: Current balance
        """
        self.balance += amount
        return self.balance


if __name__ == "__main__":
    import doctest
    import random
    from catalog import Catalog
    from course import Course
    from loan import Loan
    from person import Person
    from semester import Semester
    from staff import Staff
    from student import Student

    doctest.testmod()
