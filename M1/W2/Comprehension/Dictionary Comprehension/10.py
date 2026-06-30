
# Create a dictionary from two lists:

# keys = ["name", "age", "city"]
# values = ["Monika", 18, "Ratlam"]

keys = ["name", "age", "city"]
values = ["Monika", 18, "Ratlam"]
d={
    k:v for k,v in zip(keys,values)
}
print(d)