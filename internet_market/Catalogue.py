
class Catalogue():
    num_list = [11, 12, 23]
    catalogue_list = {
        'item1': [1, 11, 300],  # 'name' : [parent_num, num, price, *sublist]
        'item2': [1, 12, 400],
        'item3': [1, 23, 500],
        'subcat1': [1, 24.0, 0, [24.1, 24.2, 24.3]]
    }



    def add_to_catalogue(self, user, name, parent_num, num, price):
        k = 0

        if not type(user) == Admin:
            k += 1
            raise TypeError

        for i in list(Catalogue.catalogue_list.values()):
            if num == i[1]:
                k += 1

        for i in Catalogue.catalogue_list.keys():
            if name == i:
                k += 1

        if k == 0:
            Catalogue.catalogue_list[name] = [parent_num, num, price]
            Catalogue.num_list.append(num)
        else:
            print('something is not right')

        for i in Catalogue.catalogue_list:                                      # добавление в предмета субкаталог
            if Catalogue.catalogue_list[i][1] == parent_num and k == 0:
                Catalogue.catalogue_list[i][3].append(num)


    def create_subcatalogue(self, name):
        c = Catalogue.catalogue_list
        c[name][1] = float(f"{c[name][1] : .1f}")
        c[name].append([])

    @classmethod
    def changing_price(cls, name, current_price):
        Catalogue.catalogue_list[name][2] = current_price


# catalogue = Catalogue()
#
# catalogue.ceate_subcatalogue('item2')
# catalogue.add_to_catalogue(adam, 'item4', 1, 33, 1000)
# catalogue.add_to_catalogue(adam, 'item5', 24, 36, 1500)
#
# print(Catalogue.catalogue_list)
# print(Catalogue.num_list)

