# 4. Product
# Create a Product class.
# Private Attributes
# •	__name
# •	__price
# Methods
# •	get_price()
# •	set_price()
# Condition:
# •	Price should always be greater than 0.
class Product:
    def __init__(self,name,price):
        self.__name=name
        self.__price=price
    def get_price(self):
       
            return self.__price
      
    def set_price(self,nprice):
        if nprice>0:
            self.__price=nprice
        else:
            print("Invalid price! Must be greater than 0")
name=input("Enter name of product: ")
price=float(input("Enter price: "))
obj=Product(name,price)
print(obj.get_price())
obj.set_price(2000)
print(obj.get_price())


