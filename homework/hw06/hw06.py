passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            next_value = Fib(1)
            next_value.value = 1
            next_value.previous_value = 0
        elif self.value == 1 and self.previous_value == 0:
            next_value = Fib(1)
            next_value.previous_value = self.value
        else:
            next_value = Fib(self.previous_value + self.value)
            next_value.previous_value = self.value
        return next_value
        
    """
    #simplified version:
    def __init__(self, value = 0):
        self.value = 0
        self.previous = 1
    def next(self):
        next_value = Fib()
        result.value = self.value + self.previous
        result.previous = self.value
        return result
    """


    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.num = 0
        self.balance = 0
    
    def vend(self):
        if self.num == 0:
            return "Machine is out of stock."       
        elif self.balance < self.price:
            return "You must deposit ${0} more.".format(self.price - self.balance)
        elif self.balance == self.price:
            self.num -= 1
            self.balance -= self.price
            return "Here is your {0}.".format(self.product)
        else:
            self.num -= 1
            balance = self.balance
            self.balance = 0
            return "Here is your {0} and ${1} change.".format(self.product, balance - self.price)


    def restock(self, number):
        self.num += number
        return "Current {0} stock: {1}".format(self.product, self.num)

    def deposit(self, money):
        if self.num == 0:
            return "Machine is out of stock. Here is your ${0}.".format(money)
        self.balance += money
        return "Current balance: ${0}".format(self.balance)
    


