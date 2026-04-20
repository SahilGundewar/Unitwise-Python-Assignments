# This program demonstrates error handling when trying to open a file that may not exist or may have permission issues.

filename = input("Enter the file name: ")

try:
    file = open(filename, "r")
    print("File opened successfully!")
    content = file.read()
    print("File content:\n", content)
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied to read the file.")