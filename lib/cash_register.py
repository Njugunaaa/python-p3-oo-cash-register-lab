#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, items=None, total=0):
        self.total = total
        self.items = [] if items is None else items
        self.discount = discount
        self.last_transaction_amount = 0
        #To be revisited
    def add_item(self, item_name, item_price, quantity=1):
        self.last_transaction_amount = item_price * quantity
        for _ in range(quantity):
            self.items.append(item_name)
        self.total += self.last_transaction_amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount