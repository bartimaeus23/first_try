from Catalogue import Catalogue

class Order():

    def __init__(self):
        self.catalogue = Catalogue.catalogue_list
        # self.user = user
        self.order_list = []  # лист заказа

    def create_order(self, *items):
        for i in items:             #need to check if item in catalogue
            for j in self.catalogue.keys():
                if i[0] == j:
                    a = {i[0] : i[1]}
                    self.order_list.append(a)


class OrderBucket():

    def __init__(self):
        self.bucketlist = {}  # история закупок

    def add_order_tohistory(self, order):
        i = len(self.bucketlist)
        if type(order) == Order:
            self.bucketlist.update({i + 1 : order.order_list})



