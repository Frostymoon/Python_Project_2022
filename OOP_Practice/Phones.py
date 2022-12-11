from Items import *

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # calling the super() method to inheret all the attributes from __init__ in Item class
        super().__init__(name, price, quantity)

        # run validation for arguements
        assert broken_phones >= 0, f'quantity{broken_phones} is not a positive number!'

        # assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jcsPhonex10", 500, 5, 1)
phone2 = Phone("jcsPhonex20", 700, 5, 1)

print(Item.all)
print(Phone.all)