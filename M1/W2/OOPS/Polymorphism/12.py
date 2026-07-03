# 12.	Create CreditCard, UPI, and Wallet classes with a pay() method. 
# Write a function that accepts any payment object and calls pay().
class CreditCard:
    def pay(self):
        print("Using creditcard!")

class UPI:
    def pay(self):
        print("Using upi")
class Wallet:
    def pay(self):
        print("Using wallet")
def any_pay(p):
    p.pay()
c=CreditCard()
u=UPI()
w=Wallet()
l=[c,u,w]
for i in l:
    any_pay(i)

