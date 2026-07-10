# 3)	Create an abstract class Payment with an abstract method pay().
#  Implement it in UPI, CreditCard, and NetBanking.
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("UPI payment enabled")
class CreditCard(Payment):
    def pay(self):
        print("Pay through credit card")
class NetBanking(Payment):
    def pay(self):
        print("Payment through net banking")
obj=UPI()
obj.pay()

