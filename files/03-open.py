from io import open

# writing
# text = "Hello, World!"
# file = open("files/hello-world.txt", "w") # w = write, a = append, r = read
# file.write(text)
# file.close()

# reading
# file = open("files/hello-world.txt", "r")
# text = file.read()
# file.close()
# print(text)

# reading as list
# file = open("files/hello-world.txt", "r")
# text = file.readlines()
# file.close()
# print(text)  # ['Hello, World!']

# with statement is better because it automatically closes the file
# # seek method moves the cursor to a specific position in the file
# with open("files/hello-world.txt", "r") as file:
#     # __enter__ and __exit__ methods are called automatically here
#     # __enter__ opens the file
#     # __exit__ closes the file
#     print(file.readlines())
#     file.seek(0) # move the cursor to the beginning of the file
#     for line in file:
#         print(line)


# add
# file = open("files/hello-world.txt", "a+")
# file.write("\nNew line added")
# file.close()

# read and write
# with open("files/hello-world.txt", "r+") as file:  # r+ = read and write
#     text = file.readlines()
#     file.seek(0)
#     text[0] = "Modified line"
#     file.writelines(text)
