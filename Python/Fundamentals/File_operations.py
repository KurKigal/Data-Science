# Opening Files

# "w" mode: Opens the file for writing. If the file already exists, it will be overwritten.

file = open("newfile.txt", "w")
file.close()

file = open("C:/Users/pc/Desktop/newfile.txt", "w")

file = open("newfile.txt", "w", encoding="utf-8")
file.write("EMİRHAN KESER")
file.close()


# "a" mode: Opens the file for appending. The file pointer is at the end of the file if the file exists. 
# If the file does not exist, it creates a new file for writing.


file = open("newfile.txt", "w", encoding="utf-8")
file.write("Emirhan")
file.close()

file = open("newfile.txt", "a", encoding="utf-8")
file.write(" Keser")
file.close()


# "x" mode: Creates a new file. If the file already exists, the operation fails.

file = open("newfile.txt", "x", encoding="utf-8")


# "r" mode: Opens the file for reading. The file pointer is placed at the beginning of the file.
# This is the default mode.

file = open("newfile.txt")
print(file)


# Handling FileNotFoundError with try-except

try:
    file = open("newfile.txt", "r", encoding="utf-8")
    print(file)
except FileNotFoundError:
    print("File not found")
finally:
    print("File closed")
    file.close()


# Reading file with for loop

file = open("newfile.txt", "r", encoding="utf-8")
for line in file:
    print(line, end="")  # Using end="" to avoid additional new lines
file.close()


# Reading file with read() function

file = open("newfile.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()


# read() function reads the entire file if no argument is passed, 
# otherwise, it reads up to the number of characters specified.

# Using with statement for file operations

with open("newfile.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)  # Move the cursor to the beginning of the file
    print(file.tell())  # Print the current cursor position
    content2 = file.read()
    print(content2)
    # No need to explicitly close the file, with statement handles it


# "r+" mode: Opens the file for both reading and writing.

with open("newfile.txt", "r+", encoding="utf-8") as file:
    file.seek(20)  # Move the cursor to the 20th index
    file.write("test")


# Appending at the end of the file using "a" mode

with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nTunahan Keser")


# Reading the updated file

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Updating at the beginning of the file

with open("newfile.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    content = "Tunahan Keser\n" + content
    file.seek(0)
    file.write(content)


# Reading the updated file

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Updating in the middle of the file

with open("newfile.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    lines.insert(1, "Tunahan Keser\n")
    file.seek(0)
    # Using writelines() to write list of lines back to the file
    file.writelines(lines)


# Reading the updated file

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())

