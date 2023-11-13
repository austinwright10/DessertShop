'''DESSERT SHOP'''
# #Part 0 - Dessert Shop
# class Candy:
#     '''candy class with candy attributes'''
#     def __init__(self, name, weight, price_per_pound):
#         self.name = name
#         self.weight = weight
#         self.price_per_pound = price_per_pound

# class Cookie:
#     '''cookie class with cookie attributes'''
#     def __init__(self, name, quantity, price_per_dozen):
#         self.name = name
#         self.quantity = quantity
#         self.price_per_dozen = price_per_dozen

# class IceCream:
#     '''ice cream class with ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop):
#         self.name = name
#         self.scoop_count = scoop_count
#         self.price_per_scoop = price_per_scoop

# class Sundae(IceCream):
#     '''sundae class (child of ice cream class)'''
#     def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
#         super().__init__(name, scoop_count, price_per_scoop)
#         self.topping_name = topping_name
#         self.topping_price = topping_price

#Part 1 - Dessert Shop 10/2/23
# class DessertItem:
#     '''superclass for all dessert items'''
#     def __init__(self, name):
#         self.name = name
# class Candy(DessertItem):
#     '''candy class with dessertItem name and candy attributes'''
#     def __init__(self, name, candy_weight, price_per_pound):
#         super().__init__(name)
#         self.candy_weight = candy_weight
#         self.price_per_pound = price_per_pound
# class Cookie(DessertItem):
#     '''cookie class with dessertItem name and cookie attributes'''
#     def __init__(self, name, cookie_quantity, price_per_dozen):
#         super().__init__(name)
#         self.cookie_quantity = cookie_quantity
#         self.price_per_dozen = price_per_dozen
# class IceCream(DessertItem):
#     '''ice cream class with dessertItem name and ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop):
#         super().__init__(name)
#         self.scoop_count = scoop_count
#         self.price_per_scoop = price_per_scoop
# class Sundae(IceCream):
#     '''sundae class with ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
#         super().__init__(name, scoop_count, price_per_scoop)
#         self.topping_name = topping_name
#         self.topping_price = topping_price

#Dessert Shop Part 2 10/6/23
# class DessertItem:
#     '''superclass for all dessert items'''
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name
# class Candy(DessertItem):
#     '''candy class with dessertItem name and candy attributes'''
#     def __init__(self, name, candy_weight, price_per_pound):
#         super().__init__(name)
#         self.candy_weight = candy_weight
#         self.price_per_pound = price_per_pound
# class Cookie(DessertItem):
#     '''cookie class with dessertItem name and cookie attributes'''
#     def __init__(self, name, cookie_quantity, price_per_dozen):
#         super().__init__(name)
#         self.cookie_quantity = cookie_quantity
#         self.price_per_dozen = price_per_dozen
# class IceCream(DessertItem):
#     '''ice cream class with dessertItem name and ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop):
#         super().__init__(name)
#         self.scoop_count = scoop_count
#         self.price_per_scoop = price_per_scoop
# class Sundae(IceCream):
#     '''sundae class with ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
#         super().__init__(name, scoop_count, price_per_scoop)
#         self.topping_name = topping_name
#         self.topping_price = topping_price
# class Order():
#     '''order from the user'''
#     def __init__(self):
#         '''constructor for order class'''
#         self.order = []
#         self.index = 0

#     def add(self, dessert_item):
#         '''add an item to the order'''
#         if isinstance(dessert_item, DessertItem):
#             self.order.append(dessert_item)

#     def __len__(self):
#         '''returns the length of the order'''
#         return len(self.order)
#     def __iter__(self):
#         '''returns an iterator for the method'''
#         self.index  = 0
#         return self
#     def __next__(self):
#         '''goes to the next value using the iterator'''
#         if self.index < len(self.order):
#             item = self.order[self.index]
#             self.index += 1
#             return item
#         else:
#             raise StopIteration

#DESSERT SHOP PART 5 - 10/16/23
# from abc import ABC, abstractmethod
# class DessertItem(ABC):
#     '''superclass for all dessert items'''
#     def __init__(self, name):
#         self.name = name
#         self.tax_percent = 7.25
#     @abstractmethod
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return None
#     def calculate_tax(self) -> float:
#         '''calculate the tax that comes with each dessert item'''
#         cost = self.calculate_cost()
#         new_tax = (self.tax_percent/100) * cost
#         return new_tax
#     def __str__(self):
#         return self.name
# class Candy(DessertItem):
#     '''candy class with dessertItem name and candy attributes'''
#     def __init__(self, name, candy_weight, price_per_pound):
#         super().__init__(name)
#         self.candy_weight = candy_weight
#         self.price_per_pound = price_per_pound
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.candy_weight * self.price_per_pound
#     def __str__(self):
#         return (f"{self.name}, {self.candy_weight}lbs, {self.price_per_pound}/lb, \n"
#         f"${self.calculate_cost()}, ${self.calculate_tax()}")
# class Cookie(DessertItem):
#     '''cookie class with dessertItem name and cookie attributes'''
#     def __init__(self, name, cookie_quantity, price_per_dozen):
#         super().__init__(name)
#         self.cookie_quantity = cookie_quantity
#         self.price_per_dozen = price_per_dozen
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.cookie_quantity * self.price_per_dozen
#     def __str__(self):
#         return (f"{self.name}, {self.cookie_quantity} cookies, ${self.price_per_dozen}/dozen, \n"
#         f"${self.calculate_cost()}, ${self.calculate_tax()}")
# class IceCream(DessertItem):
#     '''ice cream class with dessertItem name and ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop):
#         super().__init__(name)
#         self.scoop_count = scoop_count
#         self.price_per_scoop = price_per_scoop
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.scoop_count * self.price_per_scoop
#     def __str__(self):
#         return (f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, \n"
#         f"${self.calculate_cost()}, ${self.calculate_tax()}")
# class Sundae(IceCream):
#     '''sundae class with ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
#         super().__init__(name, scoop_count, price_per_scoop)
#         self.topping_name = topping_name
#         self.topping_price = topping_price
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         ice_cream_cost = super().calculate_cost()
#         return ice_cream_cost + self.topping_price
#     def __str__(self):
#         return (f"{self.topping_name}, ${self.topping_price}, \n"
#         f"${self.calculate_cost()}, ${self.calculate_tax()}")
# class Order():
#     '''order from the user'''
#     def __init__(self):
#         '''constructor for order class'''
#         self.order = []
#         self.index = 0
#     def add(self, dessert_item):
#         '''add an item to the order'''
#         if isinstance(dessert_item, DessertItem):
#             self.order.append(dessert_item)
#     def order_cost(self):
#         '''returns the total cost for all of the items'''
#         return sum(item.calculate_cost() for item in self.order)
#     def order_tax(self):
#         '''returns the total tax for all of the items'''
#         return sum(item.calculate_tax() for item in self.order)
#     def __len__(self):
#         '''returns the length of the order'''
#         return len(self.order)
#     def __iter__(self):
#         '''returns an iterator for the method'''
#         self.index  = 0
#         return self
#     def __next__(self):
#         '''goes to the next value using the iterator'''
#         if self.index < len(self.order):
#             item = self.order[self.index]
#             self.index += 1
#             return item
#         raise StopIteration
#     def __str__(self):
#         order_str = []
#         for item in self.order:
#             item_str = f"{item.name}, {item.calculate_cost():.2f}, {item.calculate_tax():.2f}"
#             order_str.append(item_str)
#         return "\n".join(order_str)

#DESSERT SHOP PART 5 - 10/18/23
# from abc import ABC, abstractmethod
# class DessertItem(ABC):
#     '''superclass for all dessert items'''
#     def __init__(self, name):
#         self.name = name
#         self.tax_percent = 7.25
#     @abstractmethod
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return None
#     def calculate_tax(self) -> float:
#         '''calculate the tax that comes with each dessert item'''
#         cost = self.calculate_cost()
#         new_tax = (self.tax_percent/100) * cost
#         return new_tax
#     def __str__(self):
#         return self.name
# class Candy(DessertItem):
#     '''candy class with dessertItem name and candy attributes'''
#     def __init__(self, name, candy_weight, price_per_pound):
#         super().__init__(name)
#         self.candy_weight = candy_weight
#         self.price_per_pound = price_per_pound
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.candy_weight * self.price_per_pound
#     def __str__(self):
#         return (f"{self.name}, {self.candy_weight}lbs, ${self.price_per_pound}/lb, \n"
#         f"${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}")
# class Cookie(DessertItem):
#     '''cookie class with dessertItem name and cookie attributes'''
#     def __init__(self, name, cookie_quantity, price_per_dozen):
#         super().__init__(name)
#         self.cookie_quantity = cookie_quantity
#         self.price_per_dozen = price_per_dozen
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return (self.cookie_quantity * self.price_per_dozen)/12
#     def __str__(self):
#         return (f"{self.name}, {self.cookie_quantity} cookies, ${self.price_per_dozen}/dozen, \n"
#         f"${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}")
# class IceCream(DessertItem):
#     '''ice cream class with dessertItem name and ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop):
#         super().__init__(name)
#         self.scoop_count = scoop_count
#         self.price_per_scoop = price_per_scoop
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.scoop_count * self.price_per_scoop
#     def __str__(self):
#         return (f"{self.name} Ice Cream, {self.scoop_count} scoops, \n"
#         f"${self.price_per_scoop}/scoop, \n"
#         f"${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}")
# class Sundae(IceCream):
#     '''sundae class with ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
#         super().__init__(name, scoop_count, price_per_scoop)
#         self.topping_name = topping_name
#         self.topping_price = topping_price
#         self.topping_quantity = 1
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.topping_price + super().calculate_cost()
#     def __str__(self):
#         #temp_str = super().__str__()
#         return (f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, \n"
#         f"${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, \n"
#         f"{self.topping_name}, {self.topping_quantity}, ${self.topping_price}")
# class Order():
#     '''order from the user'''
#     def __init__(self):
#         '''constructor for order class'''
#         self.order = []
#         self.index = 0
#     def add(self, dessert_item):
#         '''add an item to the order'''
#         if isinstance(dessert_item, DessertItem):
#             self.order.append(dessert_item)
#     def order_cost(self):
#         '''returns the total cost for all of the items'''
#         return sum(item.calculate_cost() for item in self.order)
#     def order_tax(self):
#         '''returns the total tax for all of the items'''
#         return sum(item.calculate_tax() for item in self.order)
#     def __len__(self):
#         '''returns the length of the order'''
#         return len(self.order)
#     def __iter__(self):
#         '''returns an iterator for the method'''
#         self.index  = 0
#         return self
#     def __next__(self):
#         '''goes to the next value using the iterator'''
#         if self.index < len(self.order):
#             item = self.order[self.index]
#             self.index += 1
#             return item
#         raise StopIteration
#     def __str__(self):
#         order_str = []
#         for item in self.order:
#             item_str = item.__str__()
#             order_str.append(item_str)
#         return '\n'.join(order_str)

#Dessert shop part 6 - 10/19/23
# from abc import ABC, abstractmethod
# from packaging import Packaging
# class DessertItem(ABC, Packaging):
#     '''superclass for all dessert items'''
#     def __init__(self, name):
#         self.name = name
#         self.tax_percent = 7.25
#         self.packaging = None
#     @abstractmethod
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return None
#     def calculate_tax(self) -> float:
#         '''calculate the tax that comes with each dessert item'''
#         cost = self.calculate_cost()
#         new_tax = (self.tax_percent/100) * cost
#         return new_tax
#     def __str__(self):
#         return self.name
# class Candy(DessertItem):
#     '''candy class with dessertItem name and candy attributes'''
#     def __init__(self, name, candy_weight, price_per_pound):
#         super().__init__(name)
#         self.candy_weight = candy_weight
#         self.price_per_pound = price_per_pound
#         self.packaging = "Bag"
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.candy_weight * self.price_per_pound
#     def __str__(self):
#         return (f"{self.name} ({self.packaging}) \n"
#         f"\t{self.candy_weight} lbs. @ ${self.price_per_pound}/lb.: "
#         f"\t\t\t\t ${self.calculate_cost():.2f} \t\t[Tax: ${self.calculate_tax():.2f}]")
# class Cookie(DessertItem):
#     '''cookie class with dessertItem name and cookie attributes'''
#     def __init__(self, name, cookie_quantity, price_per_dozen):
#         super().__init__(name)
#         self.cookie_quantity = cookie_quantity
#         self.price_per_dozen = price_per_dozen
#         self.packaging = "Box"
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return (self.cookie_quantity * self.price_per_dozen)/12
#     def __str__(self):
#         return (f"{self.name} cookies ({self.packaging}) \n"
#         f"\t{self.cookie_quantity} cookies @ ${self.price_per_dozen}/dozen: "
#         f"\t\t\t ${self.calculate_cost():.2f} \t\t[Tax: ${self.calculate_tax():.2f}]")
# class IceCream(DessertItem):
#     '''ice cream class with dessertItem name and ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop):
#         super().__init__(name)
#         self.scoop_count = scoop_count
#         self.price_per_scoop = price_per_scoop
#         self.packaging = "Bowl"
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.scoop_count * self.price_per_scoop
#     def __str__(self):
#         return (f"{self.name} Ice Cream ({self.packaging}) \n"
#         f"\t{self.scoop_count} scoops @ ${self.price_per_scoop}/scoop "
#         f"\t\t\t\t ${self.calculate_cost():.2f} \t\t[Tax: ${self.calculate_tax():.2f}]")
# class Sundae(IceCream):
#     '''sundae class with ice cream attributes'''
#     def __init__(self, name, scoop_count, price_per_scoop, topping_name,
#                  topping_price):
#         super().__init__(name, scoop_count, price_per_scoop)
#         self.topping_name = topping_name
#         self.topping_price = topping_price
#         self.topping_quantity = 1
#         self.packaging = "Boat"
#     def calculate_cost(self):
#         '''calculate the cost of desired dessert item'''
#         return self.topping_price + super().calculate_cost()
#     def __str__(self):
#         #temp_str = super().__str__()
#         return (f"{self.name} ({self.packaging}) \n"
#         f"\t{self.scoop_count} scoops of {self.name.replace('Sundae', '')}ice cream "
#         f"@ ${self.price_per_scoop}/scoop \n \t{self.topping_name} topping "
#         f"@ ${self.topping_price}: \t\t\t ${self.calculate_cost():.2f} "
#         f"\t\t[Tax: ${self.calculate_tax():.2f}]")
# class Order():
#     '''order from the user'''
#     def __init__(self):
#         '''constructor for order class'''
#         self.order = []
#         self.index = 0
#     def add(self, dessert_item):
#         '''add an item to the order'''
#         if isinstance(dessert_item, DessertItem):
#             self.order.append(dessert_item)
#     def order_cost(self):
#         '''returns the total cost for all of the items'''
#         return sum(item.calculate_cost() for item in self.order)
#     def order_tax(self):
#         '''returns the total tax for all of the items'''
#         return sum(item.calculate_tax() for item in self.order)
#     def __len__(self):
#         '''returns the length of the order'''
#         return len(self.order)
#     def __iter__(self):
#         '''returns an iterator for the method'''
#         self.index  = 0
#         return self
#     def __next__(self):
#         '''goes to the next value using the iterator'''
#         if self.index < len(self.order):
#             item = self.order[self.index]
#             self.index += 1
#             return item
#         raise StopIteration
#     def __str__(self):
#         order_str = []
#         for item in self.order:
#             item_str = item.__str__()
#             order_str.append(item_str)
#         return '\n'.join(order_str)

#Dessert shop part 6 2.0 - 10/22/23
from abc import ABC, abstractmethod
from packaging import Packaging
from payable import Payable
#from combinable import Combinable
class DessertItem(ABC, Packaging):
    '''superclass for all dessert items'''
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25
        self.packaging = None
    @abstractmethod
    def calculate_cost(self):
        '''calculate the cost of desired dessert item'''
        return None
    def calculate_tax(self) -> float:
        '''calculate the tax that comes with each dessert item'''
        cost = self.calculate_cost()
        new_tax = (self.tax_percent/100) * cost
        return new_tax
    def __str__(self):
        return self.name
    def __eq__(self, other):
        '''Implement the equality (==) operator based on price'''
        return self.calculate_cost() == other.calculate_cost()
    def __ne__(self, other):
        '''Implement the inequality (!=) operator based on price'''
        return self.calculate_cost() != other.calculate_cost()
    def __lt__(self, other):
        '''Implement the less than (<) operator based on price'''
        return self.calculate_cost() < other.calculate_cost()
    def __gt__(self, other):
        '''Implement the greater than (>) operator based on price'''
        return self.calculate_cost() > other.calculate_cost()
    def __ge__(self, other):
        '''Implement the greater than or equal to (>=) operator based on price'''
        return self.calculate_cost() >= other.calculate_cost()
    def __le__(self, other):
        '''Implement the less than or equal to (<=) operator based on price'''
        return self.calculate_cost() <= other.calculate_cost()
class Candy(DessertItem):
    '''candy class with dessertItem name and candy attributes'''
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"
    def calculate_cost(self):
        '''calculate the cost of desired dessert item'''
        return self.candy_weight * self.price_per_pound
    def __str__(self):
        return (f"{self.name} ({self.packaging}), \n"
        f"\t{self.candy_weight}lbs., @ ${self.price_per_pound}/lb., "
        f"\t\t\t\t ${self.calculate_cost():.2f}, \t[Tax: ${self.calculate_tax():.2f}]")
    def can_combine(self, other: "Candy") -> bool:
        '''return True if stated conditions are satisfied'''
        if (isinstance(other, Candy) and self.name == other.name
            and self.price_per_pound == other.price_per_pound):
            return True
        return None
    def combine(self, other: "Candy") -> "Candy":
        '''combine if can_combine returns True'''
        if self.can_combine(other):
            self.candy_weight += other.candy_weight
            return self
        return None
class Cookie(DessertItem):
    '''cookie class with dessertItem name and cookie attributes'''
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
    def calculate_cost(self):
        '''calculate the cost of desired dessert item'''
        return (self.cookie_quantity * self.price_per_dozen)/12
    def __str__(self):
        return (f"{self.name} cookies ({self.packaging}), \n"
        f"\t{self.cookie_quantity} cookies, @ ${self.price_per_dozen}/dozen, "
        f"\t\t\t ${self.calculate_cost():.2f}, \t[Tax: ${self.calculate_tax():.2f}]")
    def can_combine(self, other: "Cookie") -> bool:
        '''return True if stated conditions are satisfied'''
        if (isinstance(other, Cookie) and self.name == other.name
            and self.price_per_dozen == other.price_per_dozen):
            return True
        return None
    def combine(self, other: "Cookie") -> "Cookie":
        '''combine if can_combine returns True'''
        if self.can_combine(other):
            self.price_per_dozen += other.price_per_dozen
            return self
        return None
class IceCream(DessertItem):
    '''ice cream class with dessertItem name and ice cream attributes'''
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"
    def calculate_cost(self):
        '''calculate the cost of desired dessert item'''
        return self.scoop_count * self.price_per_scoop
    def __str__(self):
        return (f"{self.name} Ice Cream ({self.packaging}), \n"
        f"\t{self.scoop_count} scoops, @ ${self.price_per_scoop}/scoop, "
        f"\t\t\t ${self.calculate_cost():.2f}, \t[Tax: ${self.calculate_tax():.2f}]")
class Sundae(IceCream):
    '''sundae class with ice cream attributes'''
    def __init__(self, name, scoop_count, price_per_scoop, topping_name,
                 topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.topping_quantity = 1
        self.packaging = "Boat"
    def calculate_cost(self):
        '''calculate the cost of desired dessert item'''
        return self.topping_price + super().calculate_cost()
    def __str__(self):
        #temp_str = super().__str__()
        return (f"{self.name} ({self.packaging}, \n"
        f"\t{self.scoop_count} scoops of {self.name.replace('Sundae', '')}ice cream, "
        f"@ ${self.price_per_scoop}/scoop, \t ${self.calculate_cost():.2f}, "
        f"\t[Tax: ${self.calculate_tax():.2f}], \n \t{self.topping_name} topping, "
        f"@ ${self.topping_price}")
class Order(Payable):
    '''order from the user'''
    def __init__(self):
        '''constructor for order class'''
        self.order = []
        self.index = 0
        self._pay_type = "CASH"
    def has_method(self, obj, method):
        '''checking if the object has the specified method'''
        return callable(getattr(obj, method))
    def add(self, dessert_item):
        '''add a dessert item to the order'''
        if isinstance(dessert_item, DessertItem):
            combined = False
            # Iterate through the existing items in the order
            for i, existing_item in enumerate(self.order):
                if (self.has_method(dessert_item, "can_combine") and
                    dessert_item.can_combine(existing_item)):
                    combined_item = existing_item.combine(dessert_item)
                    if combined_item:
                        self.order[i] = combined_item
                        combined = True
                        break
            if not combined:
                self.order.append(dessert_item)
        else:
            raise ValueError("Invalid dessert item. Only ",
                             "DessertItem objects can be added to the order.")
    def order_cost(self):
        '''returns the total cost for all of the items'''
        return sum(item.calculate_cost() for item in self.order)
    def order_tax(self):
        '''returns the total tax for all of the items'''
        return sum(item.calculate_tax() for item in self.order)
    def __len__(self):
        '''returns the length of the order'''
        return len(self.order)
    def __iter__(self):
        '''returns an iterator for the method'''
        self.index  = 0
        return self
    def __next__(self):
        '''goes to the next value using the iterator'''
        if self.index < len(self.order):
            item = self.order[self.index]
            self.index += 1
            return item
        raise StopIteration
    def get_pay_type(self) -> str:
        if self._pay_type not in ["CASH", "CARD", "PHONE"]:
            raise ValueError(f"{self._pay_type} is not a valid payment option")
        return self._pay_type
    def set_pay_type(self, payment_method: str):
        payment_options = ["CASH", "CARD", "PHONE"]
        if payment_method in payment_options:
            self._pay_type = payment_method
        else:
            raise ValueError(f"{payment_method} is not a valid payment option")
    def __str__(self):
        order_str = []
        for item in self.order:
            item_str = item.__str__()
            order_str.append(item_str)
        return '\n'.join(order_str)
    def sort(self):
        '''sorts the items in the order'''
        self.order = sorted(self.order, key=lambda x: x.calculate_cost())
