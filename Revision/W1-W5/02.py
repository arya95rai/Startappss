# I have data coming from a CSV file where every value is read as a string.
#  I want you to write a program that converts each value 
# to its appropriate Python data type and then prints both the value and its resulting type.
# Use the following input:
# data = ["25", "3.14", "True", "None", "Morgan Stanley"]
# Expected behavior:
# "25" → int
# "3.14" → float
# "True" → bool
# "None" → NoneType
# Everything else remains a string.
# Print each converted value along with its type.
data = ["25", "3.14", "True", "None", "Morgan Stanley"]
for value in data:
    if value=="None":
        converted=None
    elif value=="True":
        converted=True
    elif value=="False":
        converted=False
    elif value.isdigit():
        converted=int(value)
    else:
        try:
            converted=float(value)
        except ValueError:
            converted=value
    print(f'"{converted}" -> {type(converted).__name__}')

        





