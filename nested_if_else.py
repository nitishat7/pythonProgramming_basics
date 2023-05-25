# product1 = int(input("Enter the cost of product1 "))
# product2 = int(input("Enter the cost of product2 "))
# product3 = int(input("Enter the cost of product3 "))
# total = product1 + product2 + product3
# print("Total amount is",total)
# pay_amount = int(input("Make the payment: "))
# difference = pay_amount - total
# if difference > 0:
#     print("Thanks! Change amount is", difference)
# else:  #difference -9999
#     difference = -difference #difference = - -9=9
#     print("Insufficient Amount")
#     print("Need to pay", difference)
#     pay_amount = int(input("Make the payment: "))
#     new_difference = pay_amount - difference
#     if new_difference > 0:
#         print("Dhanyawad!")
#     else:
#         print("Ke garira??")
#
# mark1 = float(input("Enter the mark1 "))
# mark2 = float(input("Enter the mark1 "))
# mark3 = float(input("Enter the mark1 "))
# total = mark1 + mark2 + mark3
# per = total / 3
# print("Scored percentage is", per)
# if per >= 80:
#     print("Distinction")
# elif per >= 60:
#     print("1st div")
# elif per >= 45:
#     print("2nd div")
# else:
#     print("Try Again!")
#
# mark1 = float(input("Enter the mark1 "))
# mark2 = float(input("Enter the mark1 "))
# mark3 = float(input("Enter the mark1 "))
# total = mark1 + mark2 + mark3
# per = total / 3
# print("Scored percentage is", per)
# if per >= 80:
#     print("Distinction")
#     if per >= 90:
#         print("Babbal vayecha")
# if per < 80:
#     print("Try Again!")
#
# mark1 = float(input("Enter the mark1 "))
# mark2 = float(input("Enter the mark1 "))
# mark3 = float(input("Enter the mark1 "))
# total = mark1 + mark2 + mark3
# per = total / 3
# print("Scored percentage is", per)
# if per >= 80:
#     print("Distinction")
#     if per >= 90:
#         print("Babbal vayecha")
# if per < 80:
#     print("Try Again!")


mark1 = float(input("Enter the mark1 "))
mark2 = float(input("Enter the mark2 "))
mark3 = float(input("Enter the mark3 "))
total = mark1 + mark2 + mark3
per = total / 3
if mark1 <= 100 and mark2 <= 100 and mark3 <= 100:
    print("Scored percentage is", per)
    if per >= 80:
        print("Distinction")
        if per >= 90:
            print("Babbal vayecha")
    if per < 80:
        print("Try Again!")
else:
    print("Wrong Input")

mark1 = float(input("Enter the mark1 "))
mark2 = float(input("Enter the mark2 "))
mark3 = float(input("Enter the mark3 "))
total = mark1 + mark2 + mark3
per = total / 3
if mark1 <= 100 and mark2 <= 100 and mark3 <= 100:
    print("Scored percentage is", per)
    if per >= 80:
        print("Distinction")
        if per >= 90:
            print("Babbal vayecha")
    if per < 80:
        print("Try Again!")
else:
    print("Wrong Input")
