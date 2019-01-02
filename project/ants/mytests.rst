This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case Example
		>>> x = 5
		>>> x
		5


    Case AntThrower
    from ants import *
    >>> hive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> near_bee = Bee(2) # A Bee with 2 armor
    >>> far_bee = Bee(3)  # A Bee with 3 armor
    >>> ant_place = colony.places['tunnel_0_0']
    >>> ant_place.add_insect(thrower)
    >>> nearest_bee = thrower.nearest_bee(colony.hive)
    >>> print(nearest_bee)
    None