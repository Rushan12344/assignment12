try:
    age=int(input('Enter your age '))
    if age<18:
        raise ValueError(age)
except ValueError:
    print("age of" ,age,"is not allowed to have a baby")
else:
    print(age,"is allowed to have a baby")