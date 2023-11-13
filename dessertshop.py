#DessertShop Part 6 10/20/2023
'''have the functions required for our dessert shop'''
from desserts import Candy, Cookie, IceCream, Sundae, Order
#from receipt import make_receipt
class DessertShop():
    '''have the functions required for our dessert shop'''
    def __init__(self):
        self.customers: dict[str, Customer] = {}
        self.current_customer = None
        self.current_order = None
    def get_valid_integer_input(self, prompt):
        '''validate the integer input'''
        while True:
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                print("Please enter a valid number.")
    def get_valid_float_input(self, prompt):
        '''validate the float input'''
        while True:
            try:
                user_input = float(input(prompt))
                return user_input
            except ValueError:
                print("Please enter a valid number.")
    def user_prompt_candy(self):
        '''user input regarding candy'''
        name = str(input("Enter the name of the candy: "))
        price_per_pound = self.get_valid_float_input("Enter the price per pound: ")
        weight = self.get_valid_float_input("Enter the weight in pounds: ")
        return Candy(name, price_per_pound, weight)
    def user_prompt_cookie(self):
        '''user input regarding cookie'''
        type_of_cookie = str(input("Enter the type of cookie: "))
        quantity = self.get_valid_integer_input("Enter the quantity purchased: ")
        price = self.get_valid_float_input("Enter the price per dozen: ")
        return Cookie(type_of_cookie, quantity, price)
    def user_prompt_icecream(self):
        '''user input regarding icecream'''
        type_of_icecream = input(str("Enter the type of icecream: "))
        quantity = self.get_valid_integer_input("Enter the number of scoops: ")
        price = self.get_valid_float_input("Enter the price per scoop: ")
        return IceCream(type_of_icecream, quantity, price)
    def user_prompt_sundae(self):
        '''user input regarding sundae'''
        type_of_sundae = input(str("Enter the type of icecream: "))
        quantity = self.get_valid_integer_input("Enter the number of scoops: ")
        price = self.get_valid_float_input("Enter the price per scoop: ")
        topping = input(str("Enter the topping: "))
        topping_price = self.get_valid_float_input("Enter the price for the topping: ")
        return Sundae(type_of_sundae, quantity, price, topping, topping_price)
    def admin_module(self):
        '''Admin Module with additional options.'''
        while True:
            admin_prompt = '\n'.join([
                '\nAdmin Module Options:',
                '1: Shop Customer List',
                '2: Customer Order History',
                '3: Best Customer',
                '4: Exit Admin Module',
                '\nEnter your choice (1-4): '
            ])

            choice = self.get_valid_integer_input(admin_prompt)

            if choice == 1:
                self.shop_customer_list()
            elif choice == 2:
                self.customer_order_history()
            elif choice == 3:
                self.best_customer()
            elif choice == 4:
                print("Exiting Admin Module.")
                break
            else:
                print('Invalid response: Please enter a choice from the menu (1-4)')
    def shop_customer_list(self):
        '''Display the list of customers in the shop.'''
        print('\nShop Customer List:')
        for customer_id, customer in self.customers.items():
            print(f"Customer Name: {customer}\tCustomer ID: {customer_id}")
    def customer_order_history(self):
        '''Display the order history for a specific customer.'''
        customer_id = self.get_valid_integer_input("Enter the customer ID: ")
        customer = self.customers.get(customer_id)
        if customer:
            print(f'\nOrder History for {customer}:')
            for order in customer.order_history:
                print(f"Order ID: {customer_id}")
                print("----------------------------------------------------")
                print(order)
                print("----------------------------------------------------")
        else:
            print(f"No customer found with ID {customer_id}.")
    def best_customer(self):
        '''Display the best customer based on the total amount spent.'''
        if self.customers:
            best_customer_id = max(self.customers,
            key=lambda c: sum(order.order_cost() for order in self.customers[c].order_history))
            best_customer = self.customers[best_customer_id]
            print("---------------------------------------------------------")
            print(f"The Dessert Shop's most valued customer is: {best_customer.customer_name}!!")
            print("---------------------------------------------------------")
        else:
            print("No customers in the shop.")
    def payment_type(self):
        '''asks the user for the payment type'''
        order = Order()
        done: bool = False
        payment_prompt = '\n'.join([ '\n',
                                    '1: CASH',
                                    '2: CARD',
                                    '3: PHONE',
                                    '\nEnter payment method (1-3): '])
        while not done:
            choice = input(payment_prompt)
            match choice:
                case '':
                    print('Invalid response:  Please enter a choice from the menu (1-3)')
                case '1':
                    order.set_pay_type("CASH")
                    return order.get_pay_type()
                case '2':
                    order.set_pay_type("CARD")
                    return order.get_pay_type()
                case '3':
                    order.set_pay_type("PHONE")
                    return order.get_pay_type()
                case _:
                    print('Invalid response:  Please enter a choice from the menu (1-3)')

class Customer:
    '''customer class'''
    id = 1
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.order_history = []
        self.order_count = 0
        self.customer_id = Customer.id
        Customer.id += 1
    def add2history(self, order: Order) -> "Customer":
        '''add order to the order history'''
        self.order_history.append(order)
        self.order_count += 1
        return self
    def __str__(self):
        return self.customer_name


def main():
    '''putting all the pieces together'''
    done = False
    shop = DessertShop()

    while not done:
        order = Order()
        prompt = '\n'.join([
            '\n1: Candy',
            '2: Cookie',
            '3: Ice Cream',
            '4: Sundae',
            '5: Admin Module',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])
        while True:
            choice = input(prompt)
            if choice == '':
                customer_name = input("Customer Name: ")
                existing_customer = shop.customers.get(customer_name)
                if existing_customer:
                    shop.current_customer = existing_customer
                else:
                    shop.current_customer = Customer(customer_name)
                    shop.customers[shop.current_customer.customer_id] = shop.current_customer
                shop.current_customer.add2history(order)
                payment = shop.payment_type()
                break
            if choice in ['1', '2', '3', '4', '5']:
                if choice == '1':
                    item = shop.user_prompt_candy()
                    order.add(item)
                elif choice == '2':
                    item = shop.user_prompt_cookie()
                    order.add(item)
                elif choice == '3':
                    item = shop.user_prompt_icecream()
                    order.add(item)
                elif choice == '4':
                    item = shop.user_prompt_sundae()
                    order.add(item)
                elif choice == '5':
                    shop.admin_module()
            else:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()
        print("-------------------------------------Receipt------------------------------------")
        order.sort()
        print(order)
        print("--------------------------------------------------------------------------------")
        subtotal = order.order_cost()
        total_tax = order.order_tax()
        total_cost = subtotal + total_tax
        print(f"Total Number of Items in order: {str(len(order))}")
        print(f"Order Subtotals: \t\t\t\t\t ${subtotal:.2f} \t\t[Tax: ${total_tax:.2f}]")
        print(f"Order Total: \t\t\t\t\t\t\t\t     ${total_cost:.2f}")
        print("--------------------------------------------------------------------------------")
        print(f'Paid with {payment}')
        print("--------------------------------------------------------------------------------")
        print(f"Customer Name: {customer_name}\t\tCustomer ID: "
              f"{shop.current_customer.customer_id}\t\tTotal Orders: "
              f"{shop.current_customer.order_count}")
        print("\n\n")
        another_order = input("Hit Enter to start a new order. ").strip().lower()
        if another_order != "":
            done = True

    # receipt_data = []
    # receipt_data.append([f"Customer Name: {customer_name}", "", "", "", ""])
    # receipt_data.append([f"Customer ID: {shop.current_customer.customer_id}", "", "", "", ""])
    # receipt_data.append([f"Total Orders: {shop.current_customer.order_count)}", "", "", "", ""])
    # for item in order:
    #     receipt_data.append(str(item).replace('\n', '').replace('\t', '').split(', '))
    # subtotal = order.order_cost()
    # total_tax = order.order_tax()
    # total_cost = subtotal + total_tax
    # receipt_data.append(["-----------", "-----------", "-----------", "------", "------"])
    # receipt_data.append(["Total Number of Items:", str(len(order)), ""])
    # receipt_data.append(["Order Subtotal", "", "", f"${subtotal:.2f}", f"${total_tax:.2f}"])
    # receipt_data.append(["Order Total", "", "", "", f"${total_cost:.2f}"])
    # receipt_data.append(["", "", "", "", f'Paid with {payment}'])

    # make_receipt(receipt_data, "receipt.pdf")

if __name__ == "__main__":
    main()
