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


def simon(f, n):
    """
    Input: a function f: {0,1}^n → {0,1}^n.
    Assumption: there exists s in {0,1}^n such that for all x,y: [f(x) = f(y)] iff [(x+y) in {0^n, s}].
    Output: s.
    Notation: {0,1}^n is the set of bit strings of length n, s is an unknown bit string of length n, = is comparison of
              bit strings of length n, + is point-wise addition mod 2 of bit strings of length n,  and 0^n is a bit
              string of length n with all 0.
    :param f: function (black box)
    :param n: int (length of bitstring)
    :return s: string (string of bits)
    """
    # This will generate bit strings to be used for insertion into the function f for evaluation.
    bit_combo_list = list()
    binary_string = [None] * n
    generate_binary_strings(bit_combo_list, n, binary_string)

    for bit_combo_x in bit_combo_list:
        for bit_combo_y in bit_combo_list:
            # If we are looking at the same bit string, skip this iteration and continue to the next.
            if bit_combo_x == bit_combo_y:
                continue
            # If the output of our bit strings match, xor them together to find the secret string.
            x_XOR_y = list()
            if f(*bit_combo_x) == f(*bit_combo_y):
                for index in range(n):
                    x_XOR_y[n] = (bit_combo_x[n] + bit_combo_y[n]) % 2
                # Conversion from a list to a bit string
                s = "".join([str(item) for item in x_XOR_y])
                return s
        # See Note below for explanation as to the outer loop that doesn't really do anything.
        # If no 2-1 mapping was found, return the bit string of {0}^n.
        return '0' * n

    """
    Note: I moved the return statement inside the loop as I realised that we have the assumption here
          that f will always map 2-1 or 1-1. If this assumption holds true, we do not need the outer most
          loop as we can simply use the inner most loop to check all options against our first input to f.
          This means means the outer loop isn't a loop at all. I left the code with the loop structure though
          in case we are given a position where we cannot make this assumption about f.
    # If no 2-1 mapping was found, return the bit string of {0}^n.
    return '0' * n
    """