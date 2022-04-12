from Catalogue.py import Catalogue
class Order():

    def __init__(self, user):
        self.catatlogue = Catalogue.catalogueя_list
        self.user = user
        self.order_list = []  # лист заказа

    def create_order(self, *items):
        for i in items:
            a = {i[0] : i[1]}
            self.order_list.append(a)


class OrderBucket():
    bucketlist = {}                     # история закупок
    def __init__(self, user):
        self.user = user

    def add_order_tohistory(self, order):
        i = len(OrderBucket.bucketlist)
        if type(order) == Order:
            bucketlist.update({i + 1 : order.order_list})



    # def add_item(name, n):
    #     c = {name : Catalogue.catalogue_list[name]}
    #     orderlist.append(c)



