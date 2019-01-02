""" Extra questions for Lab 08 """

from lab08 import *

# OOP
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        self.buttons = [*args]

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        for button in self.buttons:
            if button.pos == info:
                button.pressed += 1
                return button.key


    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        keys = ""
        for input_value in typing_input:
            keys += self.press(input_value)
        return keys

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0


# Nonlocal
def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_counter = 0
    def make_counter():
        single_counter = 0
        def single_count(message):
            nonlocal global_counter, single_counter
            if message == "count":
                single_counter += 1
                return single_counter
            elif message == "reset":
                single_counter = 0
            elif message == "global-count":
                global_counter += 1
                return global_counter
            elif message == "global-reset":
                global_counter = 0
        return single_count
    return make_counter
        


# Lists
def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    
    if not (first[0] > sum(second) or sum(first) < second[0] or first[0] == second[0]):
        m, n = 1, 1
        while True:
            if max(m, n) <= min(len(first), len(second)):
                if sum(first[0: m]) > sum(second[0 : n]):
                    n += 1
                elif sum(first[0: m]) < sum(second[0 : n]):
                    m += 1
                else:
                    first[:m], second[:n] = second[:n], first[:m]
                    return 'Deal!'
            else:
                return "No deal!"
    else:
        return 'No deal!'


def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    
    if n <= 0 and tree.is_leaf():
        return [[tree.label]]
    paths = []
    for b in tree.branches:
        for path in long_paths(b, n-1):
            paths.append([tree.label] + path)

    # def list_to_link(lst):
    #     if len(lst) == 1:
    #         return Link(lst[0])
    #     else:
    #         return Link(lst[0], list_to_link(lst[1:]))
    # links = []
    # for path in paths:
    #     links.append(list_to_link(path))
    return paths
    
    


# Orders of Growth
def zap(n):
    i, count = 1, 0
    while i <= n:
        while i <= 5 * n:
            count += i
            print(i / 6)
            i *= 3
    return count

def boom(n):
    sum = 0
    a, b = 1, 1
    while a <= n*n:
        while b <= n*n:
            sum += (a*b)
            b += 1
        b = 0
        a += 1
    return sum
