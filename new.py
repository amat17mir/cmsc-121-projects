def add_one_and_multiply(a, x):
    """ Add 1 to a, and multiply by x"""

    ### EXERCISE 1 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = (1+a)*x

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


def within_range(x, lb, ub):
    """ Is x strictly between lb and ub?"""

    ### EXERCISE 2 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = lb < x < ub
    bool(r)

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


def number_string(x):
    if x > 0:
        s = 'POSITIVE'
    elif x < 0:
        s = 'NEGATIVE'
    else:
        s = 'ZERO'
    return s


def num_divisible(lb, ub, p, q):
    n = 0
    for i in range(lb, ub):
        if (i%p==0) and (i%q==0):
            n = n + 1
    return n


def count_negative(lst):
    n = 0
    for num in lst:
        if x < 0:
            n += x
    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n


def negate_list(lst):
    new_lst = []
    for i in lst:
        lst.append(i * -1)

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return new_lst

