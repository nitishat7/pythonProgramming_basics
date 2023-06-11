# When the error is not system generated we can customize the errors.
try:
    f_age = 22
    s_age = 30
    if f_age < s_age:
        raise Exception("Father's age is less than Son's")
except Exception as ex:
    print(ex)
else:
    print(f"Father's age is {f_age} and son's age is {s_age}")
