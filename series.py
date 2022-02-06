# Kate Pollock
# Python 310
# Fibonacci, Lesson 2

def fibonacci(n):
    """
        Summary:
        Calculate the nth value in the fibonacci series, starting with zero index

        Parameters:
        arg1 (int): parameter n

        Returns:
        int: nth value in the fibonacci

        """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n2 = 0
        n1 = 1
        for i in range(1,n):
            fib = n1 + n2
            n2 = n1
            n1 = fib
        return fib


def lucas(n):
    """
            Summary:
            Calculate the nth value in the lucas numbers series, starting with zero index

            Parameters:
            arg1 (int): parameter n

            Returns:
            int: nth value in the lucas series

            """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        n2 = 2
        n1 = 1
        for i in range(1,n):
            lucas = n1 + n2
            n2 = n1
            n1 = lucas
        return lucas


def sum_series(n, n0=0, n1=1):
    pass
