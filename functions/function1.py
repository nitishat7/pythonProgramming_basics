# create a function addition to perform an addition
a=33
b=22
def addition():
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c = a + b
    print(f"Sum is {c}")


addition()

# again create another function subtraction to perform subtraction


def sub():
    # a = int(input("Enter a number:"))
    # b = int(input("Enter a number:"))
    c = a - b
    print(f"Diff is {c}")


sub()

# these are local variable declarations we can also have a global variable
#  if the global variable is declared then it can be used anywhere in the function 
