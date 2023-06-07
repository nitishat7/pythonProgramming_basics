# def summation(a, b):
#     c = a + b
#     print(f"Sum is: {c}")
#
#
# summation(22, 33)

# function with return type

def summation(a, b):
    c = a + b
    return c


res = summation(22, 33)
print(f"Sum is {res}")
print(f"Sum is {summation(55,66)}")

assert summation(2, 3) == 5
