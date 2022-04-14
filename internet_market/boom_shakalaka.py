
from Order import *

class User():
    __last_id = 0
    user_list = dict()

    def __init__(self, name):
        User.__last_id += 13
        self.name = name
        self.id = User.__last_id
        self.order = Order()
        self.bucket = OrderBucket()

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if len(phone) == 4:
            self.__phone = phone
        else:
            print('not right amount of digits')

    def buy_smt(self, *items):
        self.order.create_order(items)
        self.bucket.add_order_tohistory(self.order)
        return "Thank for chosing us"

class Admin(User):
    __latest_id = 0
    def __init__(self, name):
        super().__init__(name)
        self.id = Admin.__latest_id


user1 = User('Vitya')
user1.phone = '9890'
user1.order.create_order(('item2', 2), ('item3', 3), ('banana', 5)) # and how you can see if we order smt that not in the
                                                                    #catalogue - it's not gonna add it to bucketlist
user1.bucket.add_order_tohistory(user1.order)
print(user1.bucket.bucketlist)
admin1 = Admin('TIKI')
admin1.phone = '6574'
Catalogue.add_to_catalogue(admin1,'clsitem4', 24, 24.8, 500, Admin)
print(Catalogue.catalogue_list)