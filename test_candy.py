'''tests for candy'''
from desserts import DessertItem, Candy, Cookie
def test_inheritance_for_candy():
    '''testing inheritance for the candy class'''
    assert issubclass(Candy, DessertItem)

def test_candy_weight():
    '''testing to see if candy class has a candy_weight attribute'''
    candy = Candy("Skittles", 400, 10)
    assert hasattr(candy, "candy_weight")

def test_candy_price_per_pound():
    '''testing to see if candy class has a price_per_pound attribute'''
    candy = Candy("Skittles", 400, 10)
    assert hasattr(candy, "price_per_pound")

def test_candy_constructor_values():
    '''testing if candy's constructor is working correctly'''
    candy = Candy("Skittles", 400, 10)
    assert candy.name == "Skittles"
    assert candy.candy_weight == 400
    assert candy.price_per_pound == 10

def test_candy_calculate_cost():
    '''testing for the cost of candy'''
    candy = Candy("Skittles", 400, 10)
    assert candy.candy_weight * candy.price_per_pound == 4000

def test_candy_calculate_tax():
    '''testing for tax for item'''
    candy = Candy("Skittles", 400, 10)
    cost = candy.calculate_cost()
    tax = candy.calculate_tax()
    assert tax == (candy.tax_percent/100) * cost

def test_candy_packaging():
    '''testing to see if candy class has a packaging attribute'''
    candy = Candy("Skittles", 400, 10)
    assert candy.packaging == "Bag"

def test_candy_can_combine():
    '''see if candy can combine'''
    candy = Candy("Skittles", 400, 10)
    candy1 = Candy("Skittles", 40, 10)
    assert candy.can_combine(candy1)

def test_candy_cannot_combine():
    '''see if candy can combine'''
    candy = Candy("Skittles", 400, 10)
    cookie = Cookie("Chocolate", 5, 10)
    assert candy.can_combine(cookie) is None

def test_candy_combine():
    '''combine two candy'''
    candy = Candy("Skittles", 400, 10)
    candy1 = Candy("Skittles", 40, 10)
    candy.combine(candy1)
    assert candy == Candy("Skittles", 440, 10)

def test_candy_combine_two_items():
    '''can't combine two different items'''
    candy = Candy("Skittles", 400, 10)
    cookie = Cookie("Chocolate", 5, 10)
    assert candy.combine(cookie) is None
