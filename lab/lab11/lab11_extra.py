""" Optional Questions for Lab 11 """

from lab11 import *

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    yield n
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        yield n

# Q6
def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    first, count = True, 1
    for val in t:
        if first:
            first, previous = False, val
        elif previous == val:
            count += 1
        else:
            previous, count = val, 1
        if count == k:
            return val
        


# Q7
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. s0 or s1 may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None)
    while True:
        if e0 == None and e1 != None:
            yield e1
            break
        elif e0 != None and e1 == None:
            yield e0
            break
        elif e1 == None and e0 == None:
            break
        elif e0 == e1:
            yield e0
            e0 = next(i0, None)
            e1 = next(i1, None)
        elif e0 < e1:
            yield e0
            e0 = next(i0, None)
        else:
            yield e1
            e1 = next(i1, None)
        

    

# Q8
def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    def naturals():
        i = 0
        while True:
            yield i
            i += 1
    for i in range(m):
        yield filter(lambda x: x % m == i, naturals())

# Q9
def zip_generator(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    zip_iter = zip(*iterables)
    try:
        while True:
            yield list(next(zip_iter))
    except StopIteration:
        pass

    
