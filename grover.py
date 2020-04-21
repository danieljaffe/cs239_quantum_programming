# Name: Daniel Jaffe
# SID: 105-363-820

"""
On a classical computer, in a classical language of your choice (such as Java, C, Python, etc), program solutions
to Simon's problem and to Grover's problem.  In each case, treat the input function f as black box that you can call
(but cannot inspect in any way at all).  Each solution will be code that includes one or more calls of f.

Submit two files, one for each problem.  Write detailed comments in the code about why it works.
"""


def generate_binary_strings(bit_combo_list, length, binary_string, index=0):
    """
    Will generate permutations of byte strings stored in a list. Note that this is done recursively
    and Python has limits to recursive calls. Without installing packages to handle working in binary
    explicitly, this is the only approach I could think of.
    :param length: int
    :param binary_string: list
    :param index: int
    :return binary_string: list
    """
    if index == length:
        bit_combo_list.append(list.copy(binary_string))
        return binary_string

    # Assign a zero to the current index and generate all other permutations for the remaining bits.
    binary_string[index] = 0
    generate_binary_strings(bit_combo_list, length, binary_string, index + 1)

    # Assign a one to the current index and generate all other permutations for the remaining bits.
    binary_string[index] = 1
    generate_binary_strings(bit_combo_list, length, binary_string, index + 1)


def grover(f, n):
    """
    Input: a function f from a bit string of length n to a single bit.
    Output: 1 if there exists a bit string x of length n such that f(x) = 1, and 0 otherwise.
    :param f: function (black box)
    :param n: int (length of bitstring)
    :return: int (0 or 1)
    """

    # This will generate bit strings to be used for insertion into the function f for evaluation.
    bit_combo_list = list()
    binary_string = [None] * n
    generate_binary_strings(bit_combo_list, n, binary_string)

    for bit_combo in bit_combo_list:
        # If f(x) = 1, return 1.
        if f(bit_combo) == 1:
            return 1

    # If f(x) for all x of {0,1}^n returns 0, then return 0.
    return 0

