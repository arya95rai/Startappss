# 16.	Create a Notification system with EmailNotification, SMSNotification, and PushNotification classes. 
# Each class should implement a send() method.
class EmailNotification:
    def send(self):
        print("Email notification")
class SMSNotification:
    def send(self):
        print("SMS notification")
class PushNotification:
    def send(self):
        print("Push notification")
def noti(n):
    n.send()
e=EmailNotification()
s=SMSNotification()
p=PushNotification()
noti(e)
noti(s)
noti(p)