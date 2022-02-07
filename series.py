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

print(lucas(5))
print(sum_series(5,2,1))
