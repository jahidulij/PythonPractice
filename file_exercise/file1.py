# Write:
#     - Open a file for writing
#     - Create a new file if doesn't exist
#     - Clears content of the file if exists
# f = open("message.txt", "w")
# # f.write("Hello File\n")
# f.write("Hello File.\n")

# Read:
#     - Opens a file for reading (default)
# f = open("message.txt", "r")
# print(f.read())

# Append:
#       - Open a file for appending at the end
#       - Create a new file if not exist
# f = open("message.txt", "a")
# f.write("This line will be appended in message.txt file.")
#
# f.close()

# with open("message.txt", "a") as f:
#     f.write("\nIt will close automatically.")

# Read multiple lines
# with open("message.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# Write multiple lines
with open("message.txt", "a") as f:
    lines = ["\nThis line will be appended", "\nThis line will be appended too"]
    f.writelines(lines)
