# 5. Mobile Phone
# Create a Mobile class.
# Attributes (8)
# •	brand
# •	model
# •	ram
# •	storage
# •	battery
# •	camera
# •	processor
# •	price
# Methods (5)
# •	call()
# •	send_message()
# •	take_photo()
# •	charge()
# •	show_specification()
class Mobile:
    def __init__(self,brand,model,ram,storage,battery,camera,processor,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.storage=storage
        self.battery=battery
        self.camera=camera
        self.processor=processor
        self.price=price
    def call(self):
        print(f"{self.brand } Calling feature")
    def send_message(self):
        print("Sending message")
    def take_photo(self):
        print("Taking photo")
    def charge(self):
        print("Mobile is charging")
    def show_specification(self):
        print("Mobile specifications")

obj=Mobile("samsung",7.3,"5gb","128gb","256mhz","50mp",3.2,20000)
obj.call()
obj.send_message()
obj.take_photo()
obj.charge()
obj.show_specification()
