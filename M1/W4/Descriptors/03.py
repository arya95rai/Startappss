# 3. Create a descriptor that stores a product's price and prevents negative values.
class MyDescriptor:
    def __get__(self,instance,owner):
        if instance.__dict__["price"]>=0:
            return instance.__dict__.get["price"]
        else:
            return "Price cannot be negative"
    def __set__(self,instance,value):
        if instance.__dict__["price"]>=0:
            instance.__dict__["price"]=1000
        else:
            return "Price cannot be negative"
    
class Product:
    price=MyDescriptor()
p1=Product()
p2=Product()
print(p1.price)
p1.price(2000)
print(p1.price)
        
        



    
