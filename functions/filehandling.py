# f = open("text.txt",)
# f.close()


# exception handling
# teef (try,except,else,finally)

try:
    a = 22/0
except Exception as ex:
    print(f"This is an error {ex}")
else:  # when the program is true
    print("We are on next stuff")
finally:  # this executes everytime
    print("This is try except block ")
print("This is demo")


# for file handling exception

try:
    f = open("text1.txt", 'r')
    # data = f.read()
    data = f.readlines()
    print(data[0])
    print(type(data))

    f.close()
except Exception as f:
    print(f"Error on file {f}")
else:
    print("This is inside file")
finally:  # this block executes everytime
    print("This is file handling")
print("This is demo")

# w writes in the file, new file is created and content inside the file is overwritten
# 'a' appends the content in the file, keeps on adding it
# x is creating a file
# r is read
