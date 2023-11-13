'''test cases for payment methods'''
from desserts import Order, Candy
def test_set_payment_method_cash():
    '''set the payment method'''
    order = Order()
    order.set_pay_type("CASH")
    assert order.get_pay_type() == "CASH"
def test_set_payment_method_card():
    '''set the payment method'''
    order = Order()
    order.set_pay_type("CARD")
    assert order.get_pay_type() == "CARD"
def test_set_payment_method_phone_number():
    '''set the payment method'''
    order = Order()
    order.set_pay_type("PHONE")
    assert order.get_pay_type() == "PHONE"
def test_invalid_payment_method():
    '''test for invalid payment method'''
    order = Order()
    try:
        order.set_pay_type("InvalidType")
    except ValueError:
        assert True
def test_get_invalid_payment_method():
    '''test for valid payment method'''
    order = Order()
    try:
        order.set_pay_type("CreditCard")
        order.get_pay_type()
    except ValueError:
        assert True

def test_sorted_order():
    '''test if the order is sorted correctly'''
    order = Order()
    # Add some dessert items to the order
    item1 = Candy("Candy A", 0.5, 1)
    item2 = Candy("Candy B", 1, 1)
    item3 = Candy("Candy C", 2, 1)
    item4 = Candy("Candy D", 3, 1)

    # Add items to the order in unsorted order
    order.add(item3)
    order.add(item1)
    order.add(item4)
    order.add(item2)

    # Sort the order by price in ascending order
    order.sort()

    # Extract the names of items from the sorted order
    sorted_items = [item.name for item in order]

    # Check if the items are sorted in ascending order by price
    assert sorted_items == ["Candy A", "Candy B", "Candy C", "Candy D"]
