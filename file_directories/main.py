import os

# Get current directory
current_dir = os.getcwd()
print(current_dir)

# Change current directory
# os.chdir("\\Users\\JahidulIslam\\PycharmProjects\\PythonPractice\\calculator")

print(os.getcwd())

with open("test.txt", "w") as f:
    f.write("This is a test file.")

print(os.listdir())

# Create a directory
# os.mkdir("test1")

# Rename directory
# os.rename("test1", "test")

# Remove a file
# os.remove("remove.txt")

# Remove a directory
# os.rmdir("test")

