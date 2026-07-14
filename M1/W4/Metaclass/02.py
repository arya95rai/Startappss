class MyMeta(type):

    def __new__(cls, name, bases, attrs):

        attrs["created_by"] = "Admin"

        return super().__new__(cls, name, bases, attrs)


class Employee(metaclass=MyMeta):
    pass


print(Employee.created_by)