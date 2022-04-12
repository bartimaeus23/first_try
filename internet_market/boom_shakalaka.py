# print(chr(1000))
# print(ord('r'))
from Order.py import *

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
    def __init(self, name):
        super().__init__(name)
        self.id = Admin.__latest_id


user1 = User('Vitya')
user1.phone = '9890'
print(user1.phone)

admin1 = Admin('TIKI')
admin1.phone = '65743'