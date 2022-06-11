import random

random.seed(2)


class Loan:
    """
    >>> import random
    >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
    >>> first_loan = Loan(4000)
    >>> first_loan
    Balance: $4000
    >>> first_loan.loan_id
    17412
    >>> second_loan = Loan(6000)
    >>> second_loan.amount
    6000
    >>> second_loan.loan_id
    22004
    >>> third_loan = Loan(1000)
    >>> third_loan.loan_id
    21124
    """

    def __init__(self, amount):
        self.loan_id = self.__getloanID
        self.amount = amount

    def __str__(self):
        return "Balance: $" + str(self.amount)

    __repr__ = __str__

    @property
    def __getloanID(self):
        return random.randint(10000, 99999)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
