class Table:
    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item=str, price=float, quantity= 1):
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

    def remove(self, item=str, price=float, quantity= 1):
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

    def get_total(self, service_percent=0.10):
        subtotal = round(self.get_subtotal(), 2)
        service_charge = round((subtotal * service_percent), 2)
        total = round((subtotal + service_charge), 2)
        total = {'Sub Total': f'£{subtotal:.2f}', 'Service Charge': f'£{service_charge:.2f}', 'Total': f'£{total:.2f}'}
        return total

    def split_bill(self):
        each_pay = round((self.get_subtotal() / self.diners), 2)
        return each_pay
