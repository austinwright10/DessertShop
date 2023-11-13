'''combinale module'''
from typing import Protocol
class Combinable(Protocol):
    '''class combinable'''
    def can_combine(self, other: "Combinable") -> bool:
        '''return True if the other is combinable'''
    def combine(self, other: "Combinable") -> "Combinable":
        '''return a new combinable that is the combination of self and other'''
