'''test cases for cookie class'''
from desserts import DessertItem, Cookie, Candy
def test_inheritance_for_cookie():
    '''testing to see if cookie is a child class of DessertItem'''
    assert issubclass(Cookie, DessertItem)

def test_cookie_quantity():
    '''testing to see if cookie class has a cookie_quantity attribute'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    assert hasattr(cookie, "cookie_quantity")

def test_cookie_price_per_dozen():
    '''testing to see if cookie class has a price_per_dozen attribute'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    assert hasattr(cookie, "price_per_dozen")

def test_cookie_constructor_values():
    '''testing to see if the cookie's class constructor is working properly'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    assert cookie.name == "SnickerDoodle"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 25

def test_cookie_calculate_value():
    '''testing for cookie's cost'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    assert (cookie.cookie_quantity * cookie.price_per_dozen)/12 == 25

def test_cookie_calculate_tax():
    '''testing for tax for item'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    cost = cookie.calculate_cost()
    tax = cookie.calculate_tax()
    assert tax == (cookie.tax_percent/100) * cost

def test_cookie_packaging():
    '''testing to see if candy class has a packaging attribute'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    assert cookie.packaging == "Box"

def test_cookie_can_combine():
    '''see if candy can combine'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    cookie1 = Cookie("SnickerDoodle", 12, 25)
    assert cookie.can_combine(cookie1)

def test_cookie_cannot_combine():
    '''see if candy can combine'''
    candy = Candy("Skittles", 400, 10)
    cookie = Cookie("Chocolate", 5, 10)
    assert cookie.can_combine(candy) is None

def test_cookie_combine():
    '''combine two candy'''
    cookie = Cookie("SnickerDoodle", 12, 25)
    cookie1 = Cookie("SnickerDoodle", 12, 25)
    cookie.combine(cookie1)
    assert cookie == Cookie("SnickerDoodle", 24, 25)

def test_cookie_combine_two_items():
    '''can't combine two different items'''
    candy = Candy("Skittles", 400, 10)
    cookie = Cookie("Chocolate", 5, 10)
    assert cookie.combine(candy) is None
