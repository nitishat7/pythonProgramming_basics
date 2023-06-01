# 1 to generate multiplication table from 1 to 10

# i = 1
# while i <= 10:
#     j = 1
#

# check whether entered number is odd or even number
# i = 1
# while i <= 3:
#     num1 = int(input("Enter a number:"))
# # num2 = int(input("Enter a number:"))
#     if num1 % 2 == 0:
#         print(num1, "Is Even number  ")
#     else:
#         print(num1, "Is odd Number")
#     i = i + 1
#
# # 4 find the largest number among entered two numbers
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# if num1 > num2:
#     largest = num1
# else:
#     largest = num2
#
# print("The largest number is:", largest)


# 6 display 1 to 50 using loop 1 2 3 4 5 ... 50

# i = 1
# while i <= 50:
#     print(i, end=' ')
#     i = i + 1
#
# # 7 display even numbers that lies in the range of 1 to 50
# print("\t\t\t")
# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i = i + 1

# 8 display odd numbers that lies in the range of 1 to 50
# print("\t\t\t")
# i = 1
# while i <= 50:
#     if i % 2 != 0:
#         print(i, end=' ')
#     i = i + 1

# 9 calculate the sum of even numbers in the range of 1 to 10
# using while loop
# i = 0
# j = 0
# while i <= 10:
#     if i % 2 == 0:
#         j = j + i
#     i = i + 1
# print("Sum of first ten even numbers:", j)

# using for loop

# i = int()
j = int()
sum_odd = int()
for i in range(0, 10):
    if i % 2 == 0:
        j = j + i
    else:
        sum_odd = sum_odd + i
print("Sum of first ten odd numbers is :", sum_odd)
print("Sum of first ten even numbers is :", j)


# 10 check which sum is greater, odd or even number sum?


