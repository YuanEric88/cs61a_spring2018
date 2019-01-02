""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    if link.rest == Link.empty:
        print(True)
        if link.first == value:
            print(True)
            link = link.rest
            print(link)
    else:
        if link.first == value:
            print(link.first)
            link = link.rest
            print(link)
            remove_all(link, value)
        else:
            remove_all(link.rest, value)

    # if link.rest != Link.empty:
    #     if link.rest.first == value:
    #         link.rest = link.rest.rest
    #         remove_all(link, value)
    #     else:
    #         remove_all(link.rest, value)

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    if not isinstance(link.first, Link):
        link.first = fn(link.first)
    else:
        deep_map_mut(fn, link.first)
    if link.rest != Link.empty:
        deep_map_mut(fn, link.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    link_rest = link.rest
    while True:
        if link_rest == link:
            return True
        else:
            link_rest = link_rest.rest
        if link_rest == Link.empty:
            return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    link_rest = link.rest
    while True:
        if link_rest == link:
            return True
        else:
            link_rest = link_rest.rest
        if link_rest == Link.empty:
            return False

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    def helper(t, rev):
        if t.is_leaf():
            pass
        else:
            labels = [b.label for b in t.branches][::-1]
            for b, r in zip(t.branches, labels):
                if rev:
                    b.label = r
                helper(b, not rev)
    helper(t, True)



# if s.first > v:
#     s.first, s.rest = v, Link(s.first, s.rest)
# elif s.first < v and empty(s.rest):
#     s.first, s.rest = 
# elif s.first < 