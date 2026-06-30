# Write a lambda function that:

# takes a price as input
# returns 10% discounted price if price ≥ 1000
# otherwise returns 5% discounted price

lam=lambda p: p-(p*0.1) if p>=1000 else p-(p*(5/100))
p=float(input("Enter price: "))
lam(p)