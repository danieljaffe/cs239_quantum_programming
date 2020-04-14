# Name: Daniel Jaffe
# SID: 105-363-820

"""
On a classical computer, in a classical language of your choice (such as C, Java, Python, etc), program solutions
to the Deutsch-Jozsa problem and to the Bernstein-Vazirani problem.  In each case, treat the input function f as
black box that you can call but cannot inspect in any way at all.  Each solution will be code that includes one or
more calls of f.

Submit two files, one for each problem.  Write detailed comments in the code about why it works.
"""


def bernstein_vazirani(f, n):
    """
    Input: a function f:  {0,1}^n → {0,1}.
    Assumption: f(x) = a * x + b.
    Output: a, b.
    Notation: {0,1}^n is the set of bit strings of length n, a is an unknown bit string of length n, * is inner product mod 2, + is addition mod 2, and b is an unknown single bit.
    :param f: lambda function
    :param n: int
    :return: int
    """

    # By first taking the inner product using the bit string of 0, we are able to solve for b as the result from such
    # an inner product would be zero.
    x = [0] * n
    a = [0] * n
    b = f(*x)
    # Here we perform the equivalence of an and operation to verify which bits are indeed 1. This brings the
    # fastest runtime of this algorithm to n
    for bit in range(n):
        x[bit] = 1
        a[bit] = (f(*x) - b) % 2
        x[bit] = 0
    return a, b
