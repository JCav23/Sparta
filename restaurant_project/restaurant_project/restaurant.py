class Table:
    def __init__(self, diners):
        self.diners = diners

    def bill(self):
        return self.bill()

    @classmethod
    def order(cls, item=str, price=float, quantity=(int, 1)):
        cls.bill.append = [{'item': item, 'price': price, 'quantity': quantity}]