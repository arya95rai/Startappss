# Write a program that:
# Takes an integer as input.
# Uses assert to ensure the number is positive.
# If the assertion passes, print:
# Valid number.
# If it fails, let Python raise the AssertionError.
n=int(input("Enter any integer: "))
assert n>=0, "Number is not positive"
print("Valid number")
