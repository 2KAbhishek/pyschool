class Course:
    """
    >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
    >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
    >>> c1 == c2
    False
    >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
    >>> c1 == c3
    True
    >>> c1
    CMPSC132(3): Programming in Python II
    >>> c2
    CMPSC360(3): Discrete Mathematics
    >>> c3
    CMPSC132(3): Programming in Python II
    >>> c1 == None
    False
    >>> print(c1)
    CMPSC132(3): Programming in Python II
    """

    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def __str__(self):
        return "{}({}): {}".format(self.cid, self.credits, self.cname)

    __repr__ = __str__

    def __eq__(self, other):
        return False if other is None else self.cid == other.cid


if __name__ == "__main__":
    import doctest

    doctest.testmod()
