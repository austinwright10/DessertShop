'''test cases for customer class'''
from dessertshop import Customer

def test_customer_has_name():
    '''testing for customer name'''
    customer = Customer("Joe")
    assert customer.customer_name == "Joe"

def test_customer_has_id():
    '''testing for customer id'''
    customer = Customer("Joe")
    assert isinstance(customer.customer_id, int)

def test_customer_unique_id():
    '''testing for customer unique id'''
    customer1 = Customer("Joe")
    customer2 = Customer("Molly")
    assert customer1.customer_id != customer2.customer_id
