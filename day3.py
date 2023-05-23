# separator

print(2001, 9, 14, sep='-')
print(2055, 2, 14, sep='/')

# asking input from the user

num1 = input("Enter a number ")
print("num1")

# implicit type conversion

num = 10
print(type(num))  # integer type

num2 = input("Enter a number")
print("num2")   # string type
print(type("num2"))

num = 10.5
print(num)
print(type(num))


num3 = input("Enter a number")
print("num3")
# res = num3 + 10  # num3 is str-type and 10 in int-type
# ,so they cannot be added
res = num3 + "This is string"  # this is concatenation
print("", res)

# type casting implementation
number = input("Enter a number ")
number = int(number)
res = number + 10
print("", res)

























