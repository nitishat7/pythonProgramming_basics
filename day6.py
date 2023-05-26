print("Hello")
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
