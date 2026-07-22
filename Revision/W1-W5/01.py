# Swap two variables without using a third variable.
a=1
b=2
print(f"a={a}, b={b}")
a=a^b
b=a^b
a=a^b
print(f"a={a}, b={b}")
