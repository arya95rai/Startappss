class MyMeta(type):

    def __new__(cls, name, bases, attrs):

        if "id" not in attrs:
            raise TypeError("Variable 'id' must be present")

        return super().__new__(cls, name, bases, attrs)


class Test(metaclass=MyMeta):

    id = 101