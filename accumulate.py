# The SICP accumulate is also know as fold right. Anything that can be
# done with fold right should be able to be done with fold left. The
# difference between the two is that one uses an iterative process and
# the other uses a recursive process. Furthermore, the two will give
# equal result for functions that is commutative. Otherwise, the
# function needs to be adjusted to produce the same/correct result.

# I am not sure if the python recursion works the way that I imagine it
# to work, and what kind of behaviors recursively calling a method would
# have. So, I will use the fold left as a simple proof of concept. 

from copy import copy

class fold_left(object):
    """ 
    I will use the python class abstraction to produce the "function"
    objects. 
    """

    def __init__(self, init, func):
        self.initial = init
        self.function = func

    def __call__(self, sequence):
        initial = copy(self.initial)
        function = copy(self.function)

        while(sequence):
            initial = function(initial, sequence.pop(0))

        return initial

if __name__ == "__main__":

    def add(a, b):
        return a + b

    sum0 = fold_left(0, add)
    assert(sum0([]) == 0)
    assert(sum0([1, 2, 3]) == 6)
    assert(sum0(list(range(10))) == 45)

    def cons(a, b):
        a.extend([b])
        return a

    append0 = fold_left([], cons)
    assert(append0([]) == [])
    assert(append0([1]) == [1])
    assert(append0([1, 2 ,3]) == [1, 2, 3])

    def predicate(a, b):
        if b > 2:
            a.extend([b])

        return a

    filter0 = fold_left([], predicate)
    assert(filter0([]) == [])
    assert(filter0([0, 1, 2]) == [])
    assert(filter0([0, 1, 2, 3]) == [3])
    assert(filter0([0, 1, 2, 3]) == [3])
