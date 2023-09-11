class Table:
    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item=str, price=float, quantity=(int, 1)):
        if len(self.bill) == 0:
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})
        else:
            ordered = False
            for bill_item in range(len(self.bill)):
                if self.bill[bill_item]['item'] == item and self.bill[bill_item]['price'] == price:
                    ordered = True
                    self.bill[bill_item]['quantity'] += quantity
            if not ordered:
                self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item=str, price=float, quantity=(int, 1)):
        ordered = False
        for bill_item in range(len(self.bill)):
            if self.bill[bill_item]['item'] == item and self.bill[bill_item]['price'] == price:
                ordered = True
                self.bill[bill_item]['quantity'] -= quantity
            if self.bill[bill_item]['item'] == item and self.bill[bill_item]['quantity'] == 0:
                print('Error, cannot remove empty item')
        if not ordered:
            print('Error, item does not exist, cannot remove item')

    def get_subtotal(self):
        subtotal = 0
        for bill_item in range(len(self.bill)):
            subtotal += (self.bill[bill_item]['price'] * self.bill[bill_item]['quantity'])
        return subtotal

