# 3.Create a Customer and Bank class. A customer can have an account in a bank. 
# Display the customer's bank information.
class Customer:
    
        def __init__(self,name):
            self.name=name

        

class Bank:
    def __init__(self,acc_no,cust_name):
         self.acc_no=acc_no
         self.cus_name=cust_name
    def details(self):
         print(f"Account number: {self.acc_no}")
         print(f"Customer name: {self.cus_name.name}")
a=Customer("Arya")
b=Bank(123,a)
b.details()



         
         

        