# Write a program that asks the user to enter a list index.
# Requirements:
# Create a list containing five numbers.
# Ask the user for an index.
# Print the element at that index.
# If the index is invalid, display an appropriate message.
# If the user enters something other than an integer, display an appropriate message.
# The program should not crash.
l=[1,2,3,4,5]
try:
    i=int(input("Enter any index of the list: "))
    print(l[i])
except ValueError:
    print("Only integer values allowed!")
except IndexError:
    print("Invalid index")
