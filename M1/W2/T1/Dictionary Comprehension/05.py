# Reverse the following dictionary:

# d = {"a":1, "b":2, "c":3}
d = {"a":1, "b":2, "c":3}
nd={
    v:k for k,v in d.items()
}
print(nd)