# Write a closure that stores a secret message and 
# provides access to it only through an inner function.
def secret(msg):
    
    def inner():
        print(msg)
    return inner
o=secret("Confidential message")
o()

