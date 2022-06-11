class Person:
    """
    >>> p1 = Person('Jason Lee', '204-99-2890')
    >>> p2 = Person('Karen Lee', '247-01-2670')
    >>> p1
    Person(Jason Lee, ***-**-2890)
    >>> p2
    Person(Karen Lee, ***-**-2670)
    >>> p3 = Person('Karen Smith', '247-01-2670')
    >>> p3
    Person(Karen Smith, ***-**-2670)
    >>> p2 == p3
    True
    >>> p1 == p2
    False
    """

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return "Person(" + self.name + ", ***-**-" + self.ssn[-4:] + ")"

    __repr__ = __str__

    def get_ssn(self):
        return self.ssn

    def __eq__(self, other):
        return False if other is None else self.ssn == other.ssn


if __name__ == "__main__":
    import doctest

    doctest.testmod()
