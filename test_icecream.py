'''test cases for icecream class'''
from desserts import DessertItem, IceCream
def test_inheritance_for_icecream():
    '''testing to see if IceCream is a child class of DessertItem'''
    assert issubclass(IceCream, DessertItem)

def test_scoop_count():
    '''testing to see if icecream class has a scoop_count attribute'''
    icecream = IceCream("Vanilla", 3, 2)
    assert hasattr(icecream, "scoop_count")

def test_price_per_scoop():
    '''testing to see if icecream class has a price_per_scoop attribute'''
    icecream = IceCream("Vanilla", 3, 2)
    assert hasattr(icecream, "price_per_scoop")

def test_icecream_constructor_values():
    '''testing to see if the icecream's class constructor is working properly'''
    icecream = IceCream("Vanilla", 3, 2)
    assert icecream.name == "Vanilla"
    assert icecream.scoop_count == 3
    assert icecream.price_per_scoop == 2

def test_icecream_calculate_cost():
    '''testing the cost of icecream'''
    icecream = IceCream("Vanilla", 3, 2)
    assert icecream.scoop_count * icecream.price_per_scoop == 6

def test_icecream_calculate_tax():
    '''testing for tax for item'''
    icecream = IceCream("Vanilla", 3, 2)
    cost = icecream.calculate_cost()
    tax = icecream.calculate_tax()
    assert tax == (icecream.tax_percent/100) * cost

def test_icecream_packaging():
    '''testing to see if candy class has a packaging attribute'''
    icecream = IceCream("Vanilla", 3, 2)
    assert icecream.packaging == "Bowl"
