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
        n_2 = 0
        n_1 = 1
        for i in range(1,n):
            fib = n_1 + n_2
            n_2 = n_1
            n_1 = fib
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
        n_2 = 2
        n_1 = 1
        for i in range(1,n):
            luc = n_1 + n_2
            n_2 = n_1
            n_1 = luc
        return luc


def sum_series(n, n0=0, n1=1):
    """
        Summary:
        Calculate the nth value in a general sum_series, that adds the
         previous 2 values, starting with zero index

        Parameters:
        arg1 (int): parameter n
        arg2 (int): optional parameter n0, default value of 0
        arg3 (int): optional parameter n1, default value of 1

        Returns:
        int: nth value in the sum_series

        """
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        n_2 = n0
        n_1 = n1
        for i in range(1,n):
            gen_sum = n_1 + n_2
            n_2 = n_1
            n_1 = gen_sum
        return gen_sum

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
