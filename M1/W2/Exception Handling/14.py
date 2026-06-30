
# 14. Using try-except-else-finally

# Write a program that:

# Takes an integer input
# Divides 100 by the number
# Uses except for errors
# Uses else to print the result
# Uses finally to print "Execution Finished"
try:
    n=int(input("Enter any integer: "))
    r=100/n
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Valid division: {r}")
finally:
    print("Execution Finished")
