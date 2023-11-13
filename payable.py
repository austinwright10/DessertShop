'''payment file'''
from typing import Protocol
class Payable(Protocol):
    '''class to handle payment'''
    def get_pay_type(self) -> str:
        '''returns the type of payment method'''
    def set_pay_type(self, payment_method) -> str:
        '''sets the type of payment method'''
