import csv

class Item:

    # class attribute
    all = []
    def __init__(self, name, price, quantity = 0):
        # Run validations to the received args
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
       

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

         # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print(items.price)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
   


print(Item.instantiate_from_csv())
