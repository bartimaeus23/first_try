class Decor:    # класс-декоратор класса
    n  = 0

    def __init__(self, n):
        Decor.n = n

    @classmethod
    def repeatit(cls, method):       # it repeats n times outcomes of each methods of decorated class
        def repeat(*args, **kwargs):
            result = method(*args, **kwargs)
            for _ in range(cls.n):
                print('vodoo')
                print(result)
        return repeat

    def __call__(self, cls):

        class NewCls:

            def __init__(self, *args, **kwargs):
                self._obj = cls(*args, **kwargs)

            def __getattribute__(self, s):
                try:
                    x = super().__getattribute__(s)
                except AttributeError:
                    pass
                else:
                    return x

                attr = self._obj.__getattribute__(s)

                if isinstance(attr, type(self.__init__)):
                    print(attr)
                    return Decor.repeatit(attr)
                else:
                    return attr
        return NewCls

@Decor(3)
class Foo():
    def boo(self, a, b):
        print(a + b, 'it is boo')
        return f'{a + b}, {b}'

    def hoo(self):
        print('it is hoo')
        return 'baloney'


f = Foo()
print(f.boo(3, 4))
print(f.hoo())    # конец удачного использования класс-декоратора Decor(n)  класса Foo
# fuck it