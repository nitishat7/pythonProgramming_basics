l1 = [["ram", 22, 75],
    ['shyam', 21, 77],
    ['hari', 22, 80]]
l1.append(['sita',19,82])
print(l1)

l1 = []
n = int(input("How many student details you want:"))
for i in range(n):
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    marks = float(input("Enter your marks:"))
    l1.append(name)
    l1.append(age)
    l1.append(marks)
print(l1)


# list as constructor
# l1 = list()
# nested list

l1 = []  # blank list
n = int(input("How many student details you want:"))
for i in range(n):
    new_list = []
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    marks = float(input("Enter your marks:"))
    new_list.append(name)
    new_list.append(age)
    new_list.append(marks)
    l1.append(new_list)
print(l1)


str1 = 'ram'
str2 = "hari"
str3 = '''sita'''
print(type(str1))
print(type(str2))
print(type(str3))

# r = raw strings
comp = r"c:\\user\\nitisha"
print(comp)
