# open file
file = open("info.txt", "w")
file.write("Hello there, Iam a FY student at MIT ADT University..\n")
file.write("This is file handling example.\n")
file.close()

# Read the file
file = open("info.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# Append to the file    
file = open("info.txt", "a")
file.write("This line is appended later.\n")
file.close()

# Read the file again to see the changes
file = open("info.txt", "r")
print("Updated Content:\n", file.read())
file.close()