# 6. File Reading Program

# Ask the user for a filename and display its contents. Handle FileNotFoundError.
try:
    file=input("Enter the name of your file: ")
    f=open(file,"r")
    print(f.read())
except FileNotFoundError:
    print("File doesn't exist!")