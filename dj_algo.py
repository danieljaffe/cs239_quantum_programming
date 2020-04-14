# Name: Daniel Jaffe
# SID: 105-363-820

"""
On a classical computer, in a classical language of your choice (such as C, Java, Python, etc), program solutions
to the Deutsch-Jozsa problem and to the Bernstein-Vazirani problem.  In each case, treat the input function f as
black box that you can call but cannot inspect in any way at all.  Each solution will be code that includes one or
more calls of f.

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
    :return: list
    """
    if index == length:
        bit_combo_list.append(list.copy(binary_string))
        return binary_string

    # Assign a zero to the current index and generate all other permutations for the remaining bits
    binary_string[index] = 0
    generate_binary_strings(bit_combo_list, length, binary_string, index + 1)

    # Assign a one to the current index and generate all other permutations for the remaining bits
    binary_string[index] = 1
    generate_binary_strings(bit_combo_list, length, binary_string, index + 1)


def deutsch_jozsa(f, n):
    """
    Input: a function f: {0,1}^n → {0,1}.
    Assumption: f is either constant or balanced.
    Output: 1 if f is constant; 0 if f is balanced.
    Notation: {0,1} is the set of bits, and {0,1}^n is the set of bit strings of length n.
    Terminology:
        Constant: f is constant if either f always outputs 0 or f always outputs 1.
        Balanced: f is balanced if f outputs 0 on exactly half of the inputs.
    :param f: lambda function
    :param n: int
    :return: int
    """

    # This will generate bit strings to be used for insertion into the function f for evaluation.
    bit_combo_list = list()
    binary_string = [None] * n
    generate_binary_strings(bit_combo_list, n, binary_string)

    # Looking for a match with the first return of function f, stored in output. If f returned a non match,
    # the function must be balanced as per the spec. If the loop completes, meaning we have tested exactly one
    # more than half the total bit combinations of length n, and the output always matches,
    # the function must be constant.
    output = None
    for position in range(2 ** (n - 1)):
        if position is 0:
            output = f(bit_combo_list[position])
            continue
        if f(bit_combo_list[position]) != output:
            print("The function f is balanced.")
            return 0
    print("The function f is constant")
    return 1
