from collections import defaultdict

sales = [
    ("Rahul", "Laptop"),
    ("Rahul", "Laptop"),
    ("Aman", "Mouse"),
    ("Rahul", "Mouse")
]

# Customer -> Product -> Count
d = defaultdict(lambda: defaultdict(int))

for customer, product in sales:
    d[customer][product] += 1

# Display
for customer, products in d.items():
    print(customer)
    for product, count in products.items():
        print(f"{product} : {count}")
    print()