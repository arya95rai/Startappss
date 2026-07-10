# 3)	Create a custom class that overrides __len__() 
# to return the number of products in a cart.
class Cart:
    def __init__(self,products):
        self.products=products
    def __len__(self):
        return len(self.products)
    def __str__(self):
        return f"Total no of products: {len(self.products)}"
obj=Cart(["Arya",1,2])
print(obj)
print(len(obj))
   

        
