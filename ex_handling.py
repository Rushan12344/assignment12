try:
    print('try block')
    x=int(input("enter num"))
    y=int(input("Enter another number"))
    z=x/y
except ZeroDivisionError:
    print("Except block")
    print("Number1 is not divisible by zero")
else: 
    print("Else block")
    print("Output",z)
finally: 
    print("Exceptional handling  program ")