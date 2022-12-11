import csv

class Item:
    pay_rate = 0.8  # this means 20% disccount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # run validation for arguements
        assert price >= 0, f'Price {price} is not a positive number!'
        assert quantity >= 0, f'quantity{quantity} is not a positive number!'

        # assign to self object
        self.name = name
        self.price = float(price)
        self.quantity = quantity
        # actions to execute

        Item.all.append(self)

    def calculate_item_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = round(self.calculate_item_price() * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # floats with .0 decimals will be ignored
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} Item('{self.name}', {self.price}, {self.quantity})"
