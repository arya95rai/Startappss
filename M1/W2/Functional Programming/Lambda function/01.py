# Write a lambda function that takes a number and returns:

# "Even" if it is divisible by 2
# "Odd" otherwise
eo=lambda x: "Even" if x%2==0 else "Odd"
print(eo(int(input(f"Enter any number: "))))