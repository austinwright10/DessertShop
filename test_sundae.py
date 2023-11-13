'''test cases for sundae class'''
from desserts import IceCream, Sundae
def test_inheritance_for_sundae():
    '''testing to see if sundae inherits correctly from icecream class'''
    assert issubclass(Sundae, IceCream)

def test_topping_name():
    '''testing to see if sundae class has an attribute of topping_name'''
    sundae = Sundae("Banana Float", 3, 2, "Chocolate", 2)
    assert hasattr(sundae, "topping_name")

def test_topping_price():
    '''testing to see if sundae class has an attribute of topping_price'''
    sundae = Sundae("Banana Float", 3, 2, "Chocolate", 2)
    assert hasattr(sundae, "topping_price")

def test_sundae_constructor_values():
    '''testing to see if the sundae's class constructor is working properly'''
    sundae = Sundae("Banana Float", 3, 2, "Chocolate", 2)
    assert sundae.name == "Banana Float"
    assert sundae.scoop_count == 3
    assert sundae.price_per_scoop == 2
    assert sundae.topping_name == "Chocolate"
    assert sundae.topping_price == 2

def test_sundae_calculate_cost():
    '''testing for the cost of sundae'''
    sundae = Sundae("Banana Float", 3, 2, "Chocolate", 2)
    icecream = IceCream("Vanilla", 3, 2)
    ice_cream_cost = icecream.calculate_cost()
    assert ice_cream_cost + sundae.topping_price == 8

def test_sundae_calculate_tax():
    '''testing for tax for item'''
    sundae = Sundae("Banana Float", 3, 2, "Chocolate", 2)
    icecream = IceCream("Vanilla", 3, 2)
    cost = sundae.calculate_cost()
    tax = sundae.calculate_tax()
    assert tax == (icecream.tax_percent/100) * cost

def test_sundae_packaging():
    '''testing to see if candy class has a packaging attribute'''
    sundae = Sundae("Banana Float", 3, 2, "Chocolate", 2)
    assert sundae.packaging == "Boat"
