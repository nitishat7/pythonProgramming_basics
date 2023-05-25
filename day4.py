
# program1
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
#
# # res = int(num1) + int(num2)
# res = num1 + num2 + num3
# print("First number is ", num1)
# print("Second number is ", num2)
# print("Third number is ", num3)
# print("Sum is ", res)
#

# Program2
# temperature = float(input("Enter today's temperature :"))
# print("Entered temperature is :", temperature)
# if temperature > 30:
#     input("It's a Hot day!!")
# if temperature < 30:
#     input("It's not a Hot Day!!")
# if temperature > 30:
#     input("It's too Hot Day!!")

# program3
# age = int(input("Enter your age: "))
# print("Your age is ", age)
# if age >= 18:
#     print("Eligible for voting")
# if age < 18:
#     print("Not Eligible for voting")

# Program4
# age = int(input("Enter your age: "))
# print("Your age is ", age)
# if age >= 18:
#     print(" Eligible for voting ")
#     if age >= 22:
#         print(" Eligible for Marriage ")
#     else:
#         print(" Not eligible for Marriage ")
# else:
#     print(" Not Eligible for voting ")


# Program3
# num1 = int(input("Enter a number"))
# if num1 > 0:
#     print("This is a positive number")
# else:
#     print("This is a negative number")

# Program4
# pant = float(input("Enter the price of pant:"))
# tShirt = float(input("Enter the price of t-shirt:"))
# socks = float(input("Enter the price of socks:"))
# belt = float(input("Enter the price of belt:"))
# shoes = float(input("Enter the price of shoes:"))
# total_amount = pant + tShirt + socks + belt + shoes
# print("Total Amount=", total_amount)
# total_amount_paid = float(input("Amount to pay:"))
#
# if total_amount < total_amount_paid:
#     change = total_amount_paid - total_amount
#     print("Your Change = ", change)
#     if total_amount == total_amount_paid:
#         print("Transaction success")
# if total_amount > total_amount_paid:
#     print("Payment insufficient!!")
#     amount_toBe_Paid = total_amount - total_amount_paid
#     print("Amount to be added : ", amount_toBe_Paid)
#     add_money = int(input("Add Amount:"))
#     if add_money > amount_toBe_Paid:
#         change2 = add_money - amount_toBe_Paid
#         print("Your change is : ", change2)
#     elif add_money == amount_toBe_Paid:
#         print("Transaction Successful Enjoy your shopping!!")
#     elif add_money < amount_toBe_Paid:
#         amount_toBe_Paid = total_amount - total_amount_paid
#         print("Amount to be added : ", amount_toBe_Paid)
#         add_money = int(input("Add Amount:"))

# Assignment
product1 = int(input("Enter the cost of product1 "))
product2 = int(input("Enter the cost of product2 "))
product3 = int(input("Enter the cost of product3 "))
total = product1 + product2 + product3
print("Total amount is",total)
pay_amount = int(input("Make the payment: "))
difference = pay_amount - total
if difference > 0:
    print("Thanks! Change amount is", difference)
else:
    print("Insufficient Amount")
    print("Need to pay", -difference)


product1 = int(input("Enter the cost of product1 "))
product2 = int(input("Enter the cost of product2 "))
product3 = int(input("Enter the cost of product3 "))
total = product1 + product2 + product3
print("Total amount is",total)
pay_amount = int(input("Make the payment: "))
difference = pay_amount - total
if difference > 0:
    print("Thanks! Change amount is", difference)
else:
    difference = -difference
    print("Insufficient Amount")
    print("Need to pay", difference)

















