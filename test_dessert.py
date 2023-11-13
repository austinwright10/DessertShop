'''Tests for dessertitem'''
from desserts import Candy

def test_dessert_item_has_name():
    '''testing to see if it has name attribute'''
    dessert_item = Candy("Skittles", 400, 10)
    assert hasattr(dessert_item, "name")

def test_dessert_item_passed_in_value():
    '''testing to see if constructor is working correctly'''
    dessert_item = Candy("Skittles", 400, 10)
    assert dessert_item.name == "Skittles"

def test_dessert_tax_percent():
    '''testing if the tax percent attribute has been put in correctly'''
    dessert_item = Candy("Skittles", 400, 10)
    assert dessert_item.tax_percent == 7.25

def test_dessert_packaging():
    '''testing if the packing attribute has been put in correctly'''
    dessert_item = Candy("Skittles", 400, 10)
    assert dessert_item.packaging == "Bag"

def test_dessert_equal():
    '''testing if item is equal to another item'''
    dessert_item1 = Candy("Skittles", 400, 10)
    dessert_item2 = Candy("Skittles", 400, 10)
    assert dessert_item1 == dessert_item2

def test_dessert_greater_than():
    '''testing if item is greater than another item'''
    dessert_item1 = Candy("Skittles", 400, 10)
    dessert_item2 = Candy("Skittles", 500, 10)
    assert dessert_item1 < dessert_item2

def test_dessert_greater_than_equal():
    '''testing if item is greater than or equal to another item'''
    dessert_item1 = Candy("Skittles", 400, 10)
    dessert_item2 = Candy("Skittles", 500, 10)
    assert dessert_item1 <= dessert_item2

def test_dessert_lesser_than():
    '''testing if item is lesser than another item'''
    dessert_item1 = Candy("Skittles", 400, 10)
    dessert_item2 = Candy("Skittles", 300, 10)
    assert dessert_item1 > dessert_item2

def test_dessert_lesser_than_equal():
    '''testing if item is lesser than or equal to another item'''
    dessert_item1 = Candy("Skittles", 400, 10)
    dessert_item2 = Candy("Skittles", 300, 10)
    assert dessert_item1 >= dessert_item2
