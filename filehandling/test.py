# f = open("test.txt")
# data = f.read()
# print(data)
# print("Need to print again")

# f1 = open("test.txt")
# data = f1.read()
# print(data)
# d1 = f1.write("\n Some contents here")
# f1 = open("test.txt")
# d = f1.read()
# print(d)


# f2 = open("test.txt")
# data = f2.write("\n Some contents")
# f2 = open('test.txt')
# data = f2.read()
# print(data)

#  f.closed = gives the value of is the file open or close

try:
    with open('test1.txt') as f:
        print(f.closed)
        data = f.read()
        print(f.mode)
        print(f.name)
        print(f.close)
except Exception as f:
    print(f)

# with open('test1.txt') as f:
#     print(f.closed)
#     data = f.read()
#     f.close()
#     print(f.mode)
#     print(f.name)
#     print(f.close)




